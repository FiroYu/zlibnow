#!/usr/bin/env python3
"""Single source of truth for the 10 language pages.

Page structure lives in TEMPLATE below; all per-language text lives in
pages_data/<lang>.json (one JSON string per generated line, keyed by the
English line number).

Edit either, then regenerate all pages from the repo root:

    py tools/build_pages.py

A {{Lnnn}} placeholder stands for line n of the generated page. If a
language's JSON lacks that key the line is omitted entirely (used where
only the root page has content, e.g. the legacy ?lang= redirect script).
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LANGS = ["en", "zh", "es", "fr", "de", "it", "ja", "ko", "ru", "ar"]
PLACEHOLDER = re.compile(r"^\{\{(L\d{3})\}\}$")

TEMPLATE = r"""<!DOCTYPE html>
{{L002}}
<head>
{{L004}}
{{L005}}
{{L006}}
{{L007}}
{{L008}}
{{L009}}
{{L010}}
{{L011}}
{{L012}}
{{L013}}
{{L014}}
    <meta charset="UTF-8">
    <!-- Analytics slot (no-cookie only): paste your provider snippet here,
         then run `py tools/build_pages.py`. See README "Analytics". -->

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#FAFEFF">
    <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
    <link rel="icon" href="/assets/favicon.ico" sizes="32x32">
    <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{{L030}}
{{L031}}
{{L032}}
    <meta name="robots" content="index, follow">
{{L034}}
    <!-- hreflang tags for international SEO -->
        <link rel="alternate" hreflang="en" href="https://zlibnow.com/">
    <link rel="alternate" hreflang="zh" href="https://zlibnow.com/zh/">
    <link rel="alternate" hreflang="es" href="https://zlibnow.com/es/">
    <link rel="alternate" hreflang="fr" href="https://zlibnow.com/fr/">
    <link rel="alternate" hreflang="de" href="https://zlibnow.com/de/">
    <link rel="alternate" hreflang="it" href="https://zlibnow.com/it/">
    <link rel="alternate" hreflang="ja" href="https://zlibnow.com/ja/">
    <link rel="alternate" hreflang="ko" href="https://zlibnow.com/ko/">
    <link rel="alternate" hreflang="ru" href="https://zlibnow.com/ru/">
    <link rel="alternate" hreflang="ar" href="https://zlibnow.com/ar/">
    <link rel="alternate" hreflang="x-default" href="https://zlibnow.com/">
    <!-- Open Graph tags -->
{{L048}}
{{L049}}
{{L050}}
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="ZLibNow">
{{L053}}
    <!-- Twitter Card tags -->
    <meta name="twitter:card" content="summary_large_image">
{{L056}}
{{L057}}
    <meta name="twitter:site" content="@zlibnow">
    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "ZLibNow",
{{L065}}
    "description": "Verified links to access the real Z-Library. Avoid fake sites and phishing attempts.",
{{L067}}
}
    </script>
    <script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
{{L077}}
            "acceptedAnswer": {
                "@type": "Answer",
{{L080}}
            }
        },
        {
            "@type": "Question",
{{L085}}
            "acceptedAnswer": {
                "@type": "Answer",
{{L088}}
            }
        },
        {
            "@type": "Question",
{{L093}}
            "acceptedAnswer": {
                "@type": "Answer",
{{L096}}
            }
        },
        {
            "@type": "Question",
{{L101}}
            "acceptedAnswer": {
                "@type": "Answer",
{{L104}}
            }
        },
        {
            "@type": "Question",
{{L109}}
            "acceptedAnswer": {
                "@type": "Answer",
{{L112}}
            }
        }
    ]
}
    </script>
    <!-- OG Image -->
    <meta property="og:image" content="https://zlibnow.com/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta name="twitter:image" content="https://zlibnow.com/og-image.png">
{{L123}}
</head>
<body>
        <!-- WeChat Browser Overlay -->
    <div class="wechat-overlay" id="wechatOverlay" role="dialog" aria-modal="true" aria-labelledby="wechatTitle">
        <div class="wechat-card">
            <div class="arrow"></div>
{{L130}}
{{L131}}
            <ol class="steps">
{{L133}}
{{L134}}
            </ol>
{{L136}}
        </div>
    </div>

<div class="container">
        <main>
                <div class="lang-switcher">
            <select onchange="location.href=this.value" aria-label="Select language">
{{L144}}
{{L145}}
{{L146}}
{{L147}}
{{L148}}
{{L149}}
{{L150}}
{{L151}}
{{L152}}
{{L153}}
            </select>
        </div>
        <header>
            <h1>ZLibNow</h1>
{{L158}}
        </header>

        <!-- Browser Access -->
        <div class="section">
{{L163}}
            <div class="links">
                <a href="https://z-lib.fm/" target="_blank" rel="noopener noreferrer">z-lib.fm</a>
                <a href="https://1lib.sk/" target="_blank" rel="noopener noreferrer">1lib.sk</a>
                <a href="https://z-lib.sk/" target="_blank" rel="noopener noreferrer">z-lib.sk</a>
{{L168}}
{{L169}}
            </div>
            <div class="links full">
{{L172}}
{{L173}}
            </div>
{{L175}}
        </div>

        <!-- Tor Access -->
        <div class="section">
{{L180}}
            <p class="tor-intro">
{{L182}}
            </p>
{{L184}}
{{L185}}
        </div>

        <!-- Apps & Telegram -->
        <div class="section">
{{L190}}
            <div class="app-links">
{{L192}}
{{L193}}
            </div>
            <div class="table-wrap">
            <table>
                <thead>
                    <tr>
{{L199}}
{{L200}}
                    </tr>
                </thead>
                <tbody>
                    <tr>
{{L205}}
                        <td>5</td>
                    </tr>
                    <tr>
{{L209}}
                        <td>10</td>
                    </tr>
                    <tr>
{{L213}}
                        <td>20</td>
                    </tr>
                </tbody>
            </table>
            </div>
{{L219}}
        </div>

        <!-- Warning -->
        <div class="warning">
{{L224}}
{{L225}}
            <div class="fake-list">
                <code>z-lib.io</code>
                <code>z-lib.id</code>
                <code>zlibrary.to</code>
            </div>
{{L231}}
        </div>

        <!-- How-To Guide -->
        <div class="section">
{{L236}}
            <div class="howto-steps">
                <div class="howto-step">
{{L239}}
                </div>
                <div class="howto-step">
{{L242}}
                </div>
                <div class="howto-step">
{{L245}}
                </div>
                <div class="howto-step">
{{L248}}
                </div>
            </div>
        </div>

        <!-- Safety Tips -->
        <div class="section">
{{L255}}
            <ul class="safety-list">
{{L257}}
{{L258}}
{{L259}}
{{L260}}
{{L261}}
            </ul>
        </div>

        <!-- FAQ -->
        <div class="section">
{{L267}}
            <div class="faq-item">
{{L269}}
{{L270}}
            </div>
            <div class="faq-item">
{{L273}}
{{L274}}
            </div>
            <div class="faq-item">
{{L277}}
{{L278}}
            </div>
            <div class="faq-item">
{{L281}}
{{L282}}
            </div>
            <div class="faq-item">
{{L285}}
{{L286}}
            </div>
        </div>

        </main>
        <footer>
            <p><a href="https://zlibnow.com/" target="_blank" rel="noopener noreferrer">zlibnow.com</a></p>
{{L293}}
        </footer>
    </div>

{{L297}}

</body></html>
"""

PLACEHOLDER_KEYS = [PLACEHOLDER.match(l).group(1) for l in TEMPLATE.split("\n") if PLACEHOLDER.match(l)]


def render(lang, data):
    out = []
    for line in TEMPLATE.split("\n"):
        m = PLACEHOLDER.match(line)
        if m:
            value = data.get(m.group(1))
            if value is not None:
                out.append(value)
        else:
            out.append(line)
    return "\n".join(out)


def main():
    for lang in LANGS:
        with open(os.path.join(HERE, "pages_data", lang + ".json"), encoding="utf-8") as f:
            data = json.load(f)
        if lang == "en":
            missing = [k for k in PLACEHOLDER_KEYS if k not in data]
            assert not missing, ("en data missing keys", missing)
        html = render(lang, data)
        rel = "index.html" if lang == "en" else lang + "/index.html"
        with open(os.path.join(ROOT, rel), "w", encoding="utf-8", newline="") as f:
            f.write(html)
        print("wrote", rel, len(html), "bytes")


if __name__ == "__main__":
    main()
