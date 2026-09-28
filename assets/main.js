// FAQ Accordion
// JS sets an exact max-height (scrollHeight) so long localized answers are never clipped;
// the CSS fallback (600px) only applies without JS.
document.querySelectorAll('.faq-question').forEach(function(q) {
    function toggleFaq() {
        var item = q.parentElement;
        var answer = item.querySelector('.faq-answer');
        var isActive = item.classList.toggle('active');
        q.setAttribute('aria-expanded', isActive);
        if (answer) {
            answer.style.maxHeight = isActive ? answer.scrollHeight + 'px' : '';
        }
    }
    q.addEventListener('click', toggleFaq);
    q.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleFaq();
        }
    });
});

// Copy buttons (Tor onion links)
(function initCopyButtons() {
    function copyText(text) {
        if (navigator.clipboard && window.isSecureContext) {
            return navigator.clipboard.writeText(text);
        }
        // Fallback for non-secure contexts / older browsers
        return new Promise(function(resolve, reject) {
            var ta = document.createElement('textarea');
            ta.value = text;
            ta.setAttribute('readonly', '');
            ta.style.position = 'fixed';
            ta.style.opacity = '0';
            document.body.appendChild(ta);
            ta.select();
            try {
                document.execCommand('copy') ? resolve() : reject(new Error('copy failed'));
            } catch (err) {
                reject(err);
            } finally {
                document.body.removeChild(ta);
            }
        });
    }

    document.querySelectorAll('.copy-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            copyText(btn.getAttribute('data-copy')).then(function() {
                var original = btn.textContent;
                btn.textContent = btn.getAttribute('data-copied') || '✓';
                btn.classList.add('copied');
                btn.disabled = true;
                setTimeout(function() {
                    btn.textContent = original;
                    btn.classList.remove('copied');
                    btn.disabled = false;
                }, 1600);
            }).catch(function() {
                // Last resort: pre-select the URL text so the user can copy manually
                var link = btn.parentElement.querySelector('.tor-link');
                if (link && window.getSelection) {
                    var range = document.createRange();
                    range.selectNodeContents(link);
                    var sel = window.getSelection();
                    sel.removeAllRanges();
                    sel.addRange(range);
                }
            });
        });
    });
})();

// WeChat Browser Detection
(function detectWeChat() {
    var ua = navigator.userAgent.toLowerCase();
    var isWeChat = ua.indexOf('micromessenger') !== -1;
    if (!isWeChat) return;

    var overlay = document.getElementById('wechatOverlay');
    var closeBtn = document.getElementById('wechatClose');
    if (!overlay || !closeBtn) return;

    // Don't re-show within the same browsing session once dismissed
    try {
        if (sessionStorage.getItem('zlibnow_wechat_dismissed')) return;
    } catch (e) { /* storage unavailable — show overlay as before */ }

    overlay.classList.add('active');
    closeBtn.focus();

    function dismiss() {
        overlay.classList.remove('active');
        try {
            sessionStorage.setItem('zlibnow_wechat_dismissed', '1');
        } catch (e) { /* ignore */ }
    }

    closeBtn.addEventListener('click', dismiss);
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && overlay.classList.contains('active')) dismiss();
    });
})();
