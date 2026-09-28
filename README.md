# ZLibNow - Z-Library Official Access Links

> Verified links to access the real Z-Library.

[English](#english) | [中文](#中文) | [Español](#español) | [Français](#français) | [Deutsch](#deutsch) | [Italiano](#italiano) | [日本語](#日本語) | [한국어](#한국어) | [Русский](#русский) | [العربية](#العربية)

---

## Official Browser Links

| | Link | Status |
|--|------|--------|
| 1 | <https://z-lib.fm> | ✅ |
| 2 | <https://1lib.sk> | ✅ |
| 3 | <https://z-lib.sk> | ✅ |
| 4 | <https://z-lib.gd> | ⚠️ Unstable |
| 5 | <https://z-lib.gl> | ⚠️ Unstable |

| Region | Link |
|--------|------|
| Italy / France / Spain | <https://z-library.ec> |

| Tool | Link |
|------|------|
| Firefox Extension | [Z-Access](https://go-to-library.sk/#browser_extensions_tab) |

---

## Tor Access

1. Download [Tor Browser](https://www.torproject.org/download/)
2. Visit: `http://bookszlibb74ugqojhzhg2a63w5i2atv5bqarulgczawnbmsb6s6qead.onion`
3. Backup: `http://loginzlib2vrak5zzpcocc3ouizykn6k5qecgj2tzlnab5wcbqhembyd.onion`

---

## Apps & Telegram Bot

| | Link |
|--|------|
| Desktop / Android App | [go-to-library.sk](https://go-to-library.sk/) |
| Telegram Bot (+10/day) | [Z-Access Telegram](https://go-to-library.sk/#telegram_bot_tab) |

| Type | Downloads / Day |
|------|-----------------|
| Guest | 5 |
| Free Account | 10 |
| Account + Telegram Bot | 20 |

New accounts get a 2-week premium trial.

---

## Fake Sites

These domains **steal credentials** and charge fake fees. **Do NOT visit:**

- ~~z-lib.io~~
- ~~z-lib.id~~
- ~~zlibrary.to~~

---

## English

China users: Use any link above with a VPN.

If a site asks for payment or donation, it is NOT the real Z-Library.

---

## 中文

中国用户：请使用以上任意链接 + VPN。

**切勿访问以下假冒网站：** ~~z-lib.io~~、~~z-lib.id~~、~~zlibrary.to~~ — 它们会窃取你的登录信息并收取虚假费用。

如果某个网站要求付款或捐款，那不是真正的 Z-Library。

---

## Español

Usuarios de China: Usen cualquiera de los enlaces anteriores con una VPN.

**No visiten estos sitios falsos:** ~~z-lib.io~~, ~~z-lib.id~~, ~~zlibrary.to~~ — roban credenciales y cobran tarifas falsas.

Si un sitio solicita pagos o donaciones, NO es el verdadero Z-Library.

---

## Français

Utilisateurs en Chine : utilisez n'importe quel lien ci-dessus avec un VPN.

**Ne visitez pas ces faux sites :** ~~z-lib.io~~, ~~z-lib.id~~, ~~zlibrary.to~~ — ils volent vos identifiants et facturent de faux frais.

Si un site demande un paiement ou un don, ce n'est PAS le vrai Z-Library.

---

## Deutsch

Nutzer aus China: Verwenden Sie einen der obigen Links mit einem VPN.

**Besuchen Sie diese falschen Seiten nicht:** ~~z-lib.io~~, ~~z-lib.id~~, ~~zlibrary.to~~ — sie stehlen Anmeldedaten und verlangen gefälschte Gebühren.

Wenn eine Seite Zahlungen oder Spenden verlangt, ist es NICHT das echte Z-Library.

---

## Italiano

Utenti in Cina: usate uno dei link sopra con una VPN.

Se siete in Italia, Francia o Spagna: provate <https://z-library.ec>

**Non visitate questi siti falsi:** ~~z-lib.io~~, ~~z-lib.id~~, ~~zlibrary.to~~ — rubano le credenziali e richiedono pagamenti falsi.

Se un sito chiede pagamenti o donazioni, NON è il vero Z-Library.

---

## 日本語

中国からのユーザー：上記のリンクをVPNと併用してください。

**以下の偽サイトにはアクセスしないでください：** ~~z-lib.io~~、~~z-lib.id~~、~~zlibrary.to~~ — ログイン情報を盗み、不正な課金を要求します。

支払いや寄付を求めるサイトは、本物の Z-Library ではありません。

---

## 한국어

중국 사용자: 위의 링크를 VPN과 함께 사용하세요.

**다음 가짜 사이트에 접속하지 마세요:** ~~z-lib.io~~, ~~z-lib.id~~, ~~zlibrary.to~~ — 자격 증명을 훔치고 가짜 수수료를 청구합니다.

결제나 기부를 요구하는 사이트는 진짜 Z-Library가 아닙니다.

---

## Русский

Пользователи из Китая: используйте любую из ссылок выше с VPN.

**Не посещайте эти поддельные сайты:** ~~z-lib.io~~, ~~z-lib.id~~, ~~zlibrary.to~~ — они крадут учётные данные и требуют поддельной оплаты.

Если сайт просит оплату или пожертвование — это НЕ настоящий Z-Library.

---

## العربية

المستخدمون من الصين: استخدم أي رابط أعلاه مع VPN.

**لا تزوروا هذه المواقع المزيفة:** ~~z-lib.io~~، ~~z-lib.id~~، ~~zlibrary.to~~ — تسرق بيانات الدخول وتفرض رسائلًا مزيفة.

إذا طلب الموقع الدفع أو التبرع، فهذا ليس Z-Library الحقيقي.

---

## About

Domain: [zlibnow.com](https://zlibnow.com)

## Link monitoring

`.github/workflows/link-check.yml` runs `tools/check_links.py` daily. Dead links
(5xx / timeouts) fail the job, so GitHub emails the owner automatically — remove
or re-verify those links, then update the "Unstable" tags on the pages if needed.
Onion links require Tor and are checked manually.

## Page generation

The 10 `index.html` pages are **generated — do not edit them directly**.
Structure lives in `tools/build_pages.py` (`TEMPLATE`), per-language text in
`tools/pages_data/<lang>.json`. Edit either, then from the repo root:

```
py tools/build_pages.py
```

All 10 pages are rewritten; review the diff and commit. A `{{Lnnn}}` placeholder
stands for line n of the generated page; a language whose JSON lacks that key
omits the line (the legacy `?lang=` redirect exists only on `/`).

## Analytics

None. Google Analytics was removed on 2026-09-28 (sets cookies, and
googletagmanager.com is unreachable in mainland China). To re-add measurement,
use a no-cookie provider — e.g. [GoatCounter](https://www.goatcounter.com)
(free for non-commercial) or Cloudflare Web Analytics — and paste its snippet
at the `Analytics slot` comment in `tools/build_pages.py`, then regenerate.
