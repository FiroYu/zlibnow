// FAQ Accordion
document.querySelectorAll('.faq-question').forEach(function(q) {
    function toggleFaq() {
        var item = q.parentElement;
        var isActive = item.classList.toggle('active');
        q.setAttribute('aria-expanded', isActive);
    }
    q.addEventListener('click', toggleFaq);
    q.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            toggleFaq();
        }
    });
});

// WeChat Browser Detection
(function detectWeChat() {
    var ua = navigator.userAgent.toLowerCase();
    var isWeChat = ua.indexOf('micromessenger') !== -1;
    if (!isWeChat) return;

    var overlay = document.getElementById('wechatOverlay');
    var closeBtn = document.getElementById('wechatClose');
    if (!overlay || !closeBtn) return;

    overlay.classList.add('active');

    closeBtn.addEventListener('click', function() {
        overlay.classList.remove('active');
    });
})();
