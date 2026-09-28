# -*- coding: utf-8 -*-
"""Verify that every link published on zlibnow.com is alive.

Exit codes: 0 = all OK/warn, 1 = at least one FAIL.
Rules:
  OK   : HTTP < 400 (3xx anti-bot challenge loops count as alive)
  WARN : 403/429 — geo/bot block; may still work for real users, human review
  FAIL : 5xx, 404, timeouts, connection errors
Onion links cannot be checked from CI (no Tor) and are intentionally omitted.
"""
import sys
import urllib.error
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

LINKS = [
    "https://z-lib.fm/",
    "https://1lib.sk/",
    "https://z-lib.sk/",
    "https://z-lib.gd/",
    "https://z-lib.gl/",
    "https://z-library.ec/",
    "https://go-to-library.sk/",
    "https://www.torproject.org/download/",
]

TIMEOUT = 20
ATTEMPTS = 2


def check(url: str) -> tuple[str, str]:
    """Return (status, detail): status in OK / WARN / FAIL."""
    last_err = ""
    for attempt in range(1, ATTEMPTS + 1):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                code = resp.code
        except urllib.error.HTTPError as e:
            code = e.code
            last_err = f"HTTP {e.code}"
        except Exception as e:  # timeout, DNS, TLS, reset...
            code = None
            last_err = str(e)[:80]

        if code is None:
            if attempt < ATTEMPTS:
                continue
            return "FAIL", last_err
        if code < 400:
            return "OK", f"HTTP {code}"
        if code in (403, 429):
            return "WARN", f"HTTP {code} (geo/bot block — verify in a real browser)"
        if attempt < ATTEMPTS:
            continue
        return "FAIL", f"HTTP {code}"
    return "FAIL", last_err  # unreachable


def main() -> int:
    failures = 0
    warnings = 0
    print(f"{'STATUS':6} {'DETAIL':<50} URL")
    for url in LINKS:
        status, detail = check(url)
        if status == "FAIL":
            failures += 1
        elif status == "WARN":
            warnings += 1
        print(f"{status:6} {detail:<50} {url}")

    print(f"\n{len(LINKS)} checked: {failures} fail, {warnings} warn")
    if failures:
        print("ACTION: remove or re-verify the failed links on the site.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
