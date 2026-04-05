# Frontend Code Review

## Review Date
2025-04-05

## Summary

### Issues Found

1. **Language Switcher Position** - The language switcher is positioned independently of the header and has no transform effects applied. The hover/focus states (lines 74-82) only change background, not position or transform. This correctly implements the requirement - the switcher does NOT move when clicked.

2. **CSS Class Name Mismatch** - Lines 151-154 define `.section-title-purple` and `.section-title-green` but the HTML uses `.section-title-blue` and `.section-title-purple`. The green class exists but is never used; the purple class exists but the CSS variable name is misleading (`--green-light` applied to purple-named class).

3. **Performance Issue** - The `@import` for Google Fonts on line 16 is render-blocking. Consider using `rel="preload"` with critical font subset or loading fonts asynchronously.

4. **Accessibility Gaps** - Several interactive elements lack proper ARIA labels:
   - External links (`.links a`, `.tor-link`, `.app-links a`) have `rel="noopener noreferrer"` but no `aria-label` for screen readers
   - The warning section's `.fake-list code` elements have hover transforms but no keyboard accessibility

5. **Mobile Optimization** - The media query at line 428 disables hover transforms for `.section` but not for links, causing inconsistent behavior. Consider disabling all transform effects on touch devices using `@media (hover: none)`.

6. **Inline Style** - Line 537 contains `style="margin-top: 1rem"` which should be moved to a CSS class for maintainability.

## Recommendations

- Fix the CSS class naming inconsistency
- Add `aria-label` to external links for better accessibility
- Use `@media (hover: none)` to disable transforms on touch devices
- Move inline styles to CSS classes
- Consider preloading Google Fonts
