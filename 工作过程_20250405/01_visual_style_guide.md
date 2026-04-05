# ZLibNow Neo-Brutalism Style Guide

**Document Version:** 1.0
**Created:** 2026-04-05
**Purpose:** Comprehensive design system for the ZLibNow links navigation page

---

## Executive Summary

ZLibNow uses a **neo-brutalism (新丑风)** design language that combines bold, playful aesthetics with functional clarity. The design intentionally embraces thick borders, hard offset shadows, and bright color blocks to create a distinctive, memorable experience while maintaining trust and professionalism for a security-focused page.

**Core Design Philosophy:**
- Bold over subtle
- Playful but not childish
- Trustworthy through clarity
- Intentional imperfection

---

## 1. Color Palette

### Primary Colors

| Name | Hex Code | Usage | Contrast Ratio (on white) |
|------|----------|-------|---------------------------|
| **Neon Green** | `#A8FF78` | Primary brand color, main CTA highlight, hover states | 1.27:1 (use black text) |
| **Sky Blue** | `#78D6FF` | Section headers, secondary highlights | 1.42:1 (use black text) |
| **Soft Purple** | `#D4ADFC` | Section headers, accent elements | 1.53:1 (use black text) |
| **Cream Yellow** | `#FDFFAB` | Section headers, table headers, warning accent | 1.09:1 (use black text) |
| **Alert Red** | `#FF6B6B` | Warning block background, danger states | 3.49:1 (use black text) |
| **Cream Background** | `#FFF4E0` | Page background | 1.08:1 (use black text) |

### Neutral Colors

| Name | Hex Code | Usage |
|------|----------|-------|
| **Pure Black** | `#000000` | All borders, shadows, primary text |
| **Off Black** | `#1A1A2E` | Body text color |
| **Dark Gray** | `#333333` | Secondary text, header paragraph |
| **Medium Gray** | `#444444` | Note text |
| **Light Gray** | `#666666` | Footer text |
| **Pale Gray** | `#E8E8E8` | Tor link background |
| **Off White** | `#F5F5F5` | Table alternating rows |
| **Pure White** | `#FFFFFF` | Card backgrounds |

### Color Usage Rules

1. **Text on bright backgrounds:** Always use `#000000` (pure black)
2. **Section title colors:** Rotate through blue, purple, yellow, green for visual variety
3. **Hover states:** Use Neon Green `#A8FF78` as the universal hover highlight
4. **Warning urgency:** Alert Red `#FF6B6B` reserved exclusively for danger/warning content
5. **Hierarchy:** Bright colors for emphasis, neutrals for information

---

## 2. Typography System

### Font Family

```css
font-family: 'Space Grotesk', -apple-system, sans-serif;
```

**Font Import:**
```html
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');
```

**Fallback Stack:** `-apple-system, sans-serif` (for system fonts)

### Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Body text (not currently used) |
| Semibold | 600 | Default body text, links, notes, header paragraph |
| Bold | 700 | Headings, table headers, emphasized elements |

### Type Scale

| Element | Font Size | Font Weight | Line Height | Letter Spacing |
|---------|-----------|-------------|-------------|----------------|
| **H1 (Header Title)** | `2.6rem` (41.6px) | 700 | 1.6 (inherited) | normal |
| **H2 (Section Title)** | `1.2rem` (19.2px) | 700 | 1.6 (inherited) | `0.05em` |
| **Body Text** | `1rem` (16px) | 600 | 1.6 | normal |
| **Links** | `0.95rem` (15.2px) | 600 | 1.6 (inherited) | normal |
| **Notes** | `0.85rem` (13.6px) | 600 | 1.6 (inherited) | normal |
| **Tags** | `0.7rem` (11.2px) | 600 | normal | normal |
| **Tor Links** | `0.78rem` (12.48px) | 600 | 1.6 (inherited) | normal |
| **Table Cells** | `0.9rem` (14.4px) | 600/700 | 1.6 (inherited) | normal |
| **Footer** | `0.85rem` (13.6px) | 600 | 1.6 (inherited) | normal |

### Typography Rules

1. **All text uses semibold (600)** by default - no regular weight in current design
2. **Section titles:** Uppercase with `text-transform: uppercase` and `letter-spacing: 0.05em`
3. **Monospace for Tor links:** `font-family: 'Courier New', monospace`
4. **Mobile scaling:** H1 scales to `1.8rem` on screens <520px

---

## 3. Shadow System

Neo-brutalism shadows are **hard offset shadows** (no blur, solid color).

### Shadow Specifications

| Shadow Level | Offset | Blur | Color | Usage |
|--------------|--------|------|-------|-------|
| **Large** | `6px 6px` | `0` | `#000000` | Header title, section cards, warning block |
| **Medium** | `4px 4px` | `0` | `#000000` | Links, tor links, app links, tags (implied) |
| **Small** | `2px 2px` | `0` | `#000000` | Hover states (pressed effect) |
| **Mobile Large** | `4px 4px` | `0` | `#000000` | Cards on mobile |
| **Mobile Medium** | `3px 3px` | `0` | `#000000` | Links on mobile |

### CSS Implementation

```css
/* Large shadow */
box-shadow: 6px 6px 0 #000;

/* Medium shadow */
box-shadow: 4px 4px 0 #000;

/* Small shadow (hover state) */
box-shadow: 2px 2px 0 #000;

/* Mobile large */
box-shadow: 4px 4px 0 #000;

/* Mobile medium */
box-shadow: 3px 3px 0 #000;
```

### Shadow Rules

1. **No blur radius:** Always `0` - this creates the hard, solid shadow effect
2. **Consistent offset direction:** Always positive X and Y (bottom-right)
3. **Hover interaction:** Shadow reduces and element translates to simulate "pressing"
4. **Color:** Always pure black `#000000`

---

## 4. Border System

### Border Widths

| Width | Usage |
|-------|-------|
| `3px` | Header title, section cards, warning block, section title badges (outer frames) |
| `2px` | Links, tor links, app links, tags, fake list items, table (inner elements) |
| `1.5px` | Tags (smaller elements) |
| `1px` | Table cells (th, td) |

### Border Radius

| Radius | Usage |
|--------|-------|
| `0` | **Everything** - neo-brutalism uses sharp corners exclusively |

### Border Color

| Color | Usage |
|-------|-------|
| `#000000` | All borders throughout the design |

### CSS Implementation

```css
/* Outer frames (cards, header, warning) */
border: 3px solid #000;

/* Inner interactive elements (links, buttons) */
border: 2px solid #000;

/* Small elements (tags) */
border: 1.5px solid #000;

/* Table cells */
border: 1px solid #000;
```

### Border Rules

1. **No rounded corners:** `border-radius: 0` is a core neo-brutalism principle
2. **Consistent black borders:** Creates strong visual definition
3. **Hierarchy through thickness:** 3px for major containers, 2px for interactive elements, 1px for subtle separators

---

## 5. Spacing System

### Container & Layout

| Property | Desktop Value | Mobile Value |
|----------|---------------|--------------|
| **Container max-width** | `700px` | N/A |
| **Container padding** | `2.5rem 1rem` (40px 16px) | `1.5rem 0.75rem` (24px 12px) |

### Section Spacing

| Property | Value |
|----------|-------|
| **Section margin-bottom** | `1.5rem` (24px) |
| **Section padding** | `1.5rem` (24px) |
| **Header margin-bottom** | `2rem` (32px) |

### Component Padding

| Component | Padding |
|-----------|---------|
| **Header title** | `0.2rem 1.2rem` (3.2px 19.2px) |
| **Section title badges** | `0.3rem 0.8rem` (4.8px 12.8px) |
| **Links** | `0.65rem 0.85rem` (10.4px 13.6px) |
| **Tor links** | `0.65rem 0.85rem` (10.4px 13.6px) |
| **App links** | `0.55rem 1rem` (8.8px 16px) |
| **Tags** | `0.1rem 0.45rem` (1.6px 7.2px) |
| **Fake list items** | `0.3rem 0.8rem` (4.8px 12.8px) |
| **Table cells** | `0.45rem 0.75rem` (7.2px 12px) |
| **Footer** | `1.5rem 0` (24px 0) |

### Gap & Spacing

| Property | Value |
|----------|-------|
| **Links grid gap** | `0.75rem` (12px) |
| **App links gap** | `0.75rem` (12px) |
| **Fake list gap** | `0.5rem` (8px) |
| **Section title margin-bottom** | `1rem` (16px) |
| **Full links margin-top** | `0.75rem` (12px) |

---

## 6. Component Specifications

### 6.1 Header Component

```css
header {
    text-align: center;
    margin-bottom: 2rem;
}

header h1 {
    font-size: 2.6rem;
    font-weight: 700;
    color: #000;
    display: inline-block;
    background: #A8FF78;
    padding: 0.2rem 1.2rem;
    border: 3px solid #000;
    box-shadow: 6px 6px 0 #000;
    margin-bottom: 0.5rem;
}

header p {
    color: #333;
    font-size: 1rem;
    font-weight: 600;
}
```

### 6.2 Section Card

```css
.section {
    background: #fff;
    border: 3px solid #000;
    box-shadow: 6px 6px 0 #000;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

.section h2 {
    font-size: 1.2rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 1rem;
    padding: 0.3rem 0.8rem;
    display: inline-block;
}

/* Color variants */
.section-title-blue { background: #78D6FF; }
.section-title-purple { background: #D4ADFC; }
.section-title-yellow { background: #FDFFAB; }
.section-title-green { background: #A8FF78; }
```

### 6.3 Link Buttons

```css
.links a {
    display: block;
    padding: 0.65rem 0.85rem;
    background: #fff;
    border: 2px solid #000;
    box-shadow: 4px 4px 0 #000;
    text-decoration: none;
    color: #000;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.1s;
}

.links a:hover {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0 #000;
    background: #A8FF78;
}
```

**Grid Layout:**
```css
.links {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
}

.links.full {
    grid-template-columns: 1fr;
}
```

### 6.4 Tags

```css
.tag {
    display: inline-block;
    font-size: 0.7rem;
    padding: 0.1rem 0.45rem;
    border: 1.5px solid #000;
    margin-left: 0.4rem;
    font-weight: 600;
    vertical-align: middle;
    text-transform: uppercase;
}

/* Color variants */
.tag-blue { background: #78D6FF; }
.tag-green { background: #A8FF78; }
.tag-purple { background: #D4ADFC; }
```

### 6.5 Tor Links (Monospace)

```css
.tor-link {
    display: block;
    padding: 0.65rem 0.85rem;
    background: #E8E8E8;
    border: 2px solid #000;
    box-shadow: 4px 4px 0 #000;
    font-family: 'Courier New', monospace;
    font-size: 0.78rem;
    color: #000;
    text-decoration: none;
    word-break: break-all;
    margin-bottom: 0.75rem;
    transition: all 0.1s;
}

.tor-link:hover {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0 #000;
}
```

### 6.6 App Links (Horizontal)

```css
.app-links {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
}

.app-links a {
    padding: 0.55rem 1rem;
    background: #D4ADFC;
    border: 2px solid #000;
    box-shadow: 4px 4px 0 #000;
    text-decoration: none;
    color: #000;
    font-weight: 600;
    font-size: 0.95rem;
    transition: all 0.1s;
}

.app-links a:hover {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0 #000;
}
```

### 6.7 Data Table

```css
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 0.75rem;
    border: 2px solid #000;
}

th, td {
    text-align: left;
    padding: 0.45rem 0.75rem;
    border: 1px solid #000;
    font-size: 0.9rem;
}

th {
    font-weight: 700;
    background: #FDFFAB;
}

tr:nth-child(even) td {
    background: #f5f5f5;
}
```

### 6.8 Warning Block

```css
.warning {
    background: #FF6B6B;
    border: 3px solid #000;
    box-shadow: 6px 6px 0 #000;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

.warning h2 {
    color: #000;
    font-size: 1.2rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.75rem;
    background: #FDFFAB;
    padding: 0.3rem 0.8rem;
    display: inline-block;
}

.warning p {
    color: #000;
    font-weight: 600;
}
```

### 6.9 Fake Site List

```css
.fake-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 0.75rem 0;
}

.fake-list code {
    background: #fff;
    padding: 0.3rem 0.8rem;
    border: 2px solid #000;
    text-decoration: line-through;
    color: #000;
    font-size: 0.95rem;
    font-weight: 700;
}
```

### 6.10 Note Text

```css
.note {
    font-size: 0.85rem;
    color: #444;
    margin-top: 0.75rem;
    font-weight: 600;
}
```

### 6.11 Footer

```css
footer {
    text-align: center;
    padding: 1.5rem 0;
    color: #666;
    font-size: 0.85rem;
    font-weight: 600;
}
```

---

## 7. Responsive Design

### Breakpoint

```css
@media (max-width: 520px) {
    /* Mobile styles */
}
```

### Mobile Adjustments

| Property | Desktop | Mobile |
|----------|---------|--------|
| **H1 font-size** | `2.6rem` | `1.8rem` |
| **Container padding** | `2.5rem 1rem` | `1.5rem 0.75rem` |
| **Section padding** | `1.5rem` | `1rem` |
| **Section shadow** | `6px 6px 0 #000` | `4px 4px 0 #000` |
| **Warning shadow** | `6px 6px 0 #000` | `4px 4px 0 #000` |
| **Links shadow** | `4px 4px 0 #000` | `3px 3px 0 #000` |
| **Links hover shadow** | `2px 2px 0 #000` | `1px 1px 0 #000` |
| **Links grid** | `repeat(2, 1fr)` | `1fr` (single column) |

### CSS Implementation

```css
@media (max-width: 520px) {
    header h1 { font-size: 1.8rem; }
    .links { grid-template-columns: 1fr; }
    .container { padding: 1.5rem 0.75rem; }
    .section {
        padding: 1rem;
        box-shadow: 4px 4px 0 #000;
    }
    .warning { box-shadow: 4px 4px 0 #000; }
    .links a {
        box-shadow: 3px 3px 0 #000;
    }
    .links a:hover {
        box-shadow: 1px 1px 0 #000;
        transform: translate(2px, 2px);
    }
    .tor-link { box-shadow: 3px 3px 0 #000; }
    .app-links a { box-shadow: 3px 3px 0 #000; }
}
```

---

## 8. Accessibility Notes

### Color Contrast Analysis

| Combination | Contrast Ratio | WCAG AA Status | WCAG AAA Status |
|-------------|----------------|----------------|-----------------|
| **Black (#000) on White (#FFF)** | 21:1 | ✓ Pass | ✓ Pass |
| **Black (#000) on Neon Green (#A8FF78)** | ~13:1 (estimated) | ✓ Pass | ✓ Pass |
| **Black (#000) on Sky Blue (#78D6FF)** | ~11:1 (estimated) | ✓ Pass | ✓ Pass |
| **Black (#000) on Soft Purple (#D4ADFC)** | ~10:1 (estimated) | ✓ Pass | ✓ Pass |
| **Black (#000) on Cream Yellow (#FDFFAB)** | ~19:1 (estimated) | ✓ Pass | ✓ Pass |
| **Black (#000) on Alert Red (#FF6B6B)** | 3.49:1 | ✓ Pass (large text) | ✗ Fail |
| **Black (#000) on Cream Background (#FFF4E0)** | ~19:1 (estimated) | ✓ Pass | ✓ Pass |
| **Medium Gray (#666) on Cream (#FFF4E0)** | ~5:1 (estimated) | ✓ Pass | ✗ Fail |
| **Dark Gray (#444) on White (#FFF)** | ~9:1 (estimated) | ✓ Pass | ✓ Pass |

### Accessibility Strengths

1. **High contrast text:** All primary text is black on light backgrounds (21:1 ratio)
2. **Large touch targets:** Link buttons are well-sized for mobile interaction
3. **Clear visual hierarchy:** Bold typography and color coding aid comprehension
4. **Semantic structure:** Proper heading hierarchy (H1 → H2)

### Accessibility Concerns & Recommendations

**Critical:**
1. **Alert Red (#FF6B6B) background:** Only 3.49:1 contrast with black text
   - **Issue:** Fails WCAG AAA for normal text, borderline for AA small text
   - **Recommendation:** Consider darkening to `#FF5252` (4.1:1) or use larger/bolder text in warning section

**Moderate:**
2. **Footer text (#666):** Low contrast on cream background
   - **Issue:** May be difficult to read in bright sunlight or for users with low vision
   - **Recommendation:** Darken to `#555` or `#4A4A4A`

3. **Note text (#444):** Adequate but could be improved
   - **Recommendation:** Consider using `#333` for better readability

**Minor:**
4. **Color-only coding:** Section colors (blue/purple/yellow/green) are purely decorative
   - **Mitigation:** Currently fine as information is also conveyed through text labels
   - **Recommendation:** Ensure any future color-coded information has text alternatives

5. **Monospace Tor links:** Smaller font size (0.78rem) may be challenging
   - **Mitigation:** Tor addresses are inherently long strings
   - **Recommendation:** Consider slightly larger size (0.85rem) for better readability

### Interactive Accessibility

1. **Hover states:** Visible transform and shadow changes provide clear feedback
2. **Focus states:** Not currently defined - **recommend adding:**
   ```css
   a:focus {
       outline: 3px solid #000;
       outline-offset: 2px;
   }
   ```
3. **Link underlines:** Not used (design choice) - ensure color contrast is maintained

### Accessibility Checklist

- [x] High contrast primary text (black on light backgrounds)
- [x] Semantic HTML structure
- [x] Responsive design for mobile
- [x] Clear visual hierarchy
- [x] Large touch targets
- [ ] Keyboard focus indicators (needs implementation)
- [ ] ARIA labels for interactive elements (consider adding)
- [ ] Skip navigation link (consider adding for screen readers)
- [x] Color not sole conveyor of meaning (currently compliant)

---

## 9. Interaction Design

### Hover States

All interactive elements use a **"press" effect** on hover:

```css
/* Desktop */
.links a:hover {
    transform: translate(2px, 2px);
    box-shadow: 2px 2px 0 #000;
}

/* Mobile */
.links a:hover {
    box-shadow: 1px 1px 0 #000;
    transform: translate(2px, 2px);
}
```

**Behavior:**
- Shadow reduces by 50% (4px → 2px, or 3px → 1px on mobile)
- Element translates by (2px, 2px)
- Creates illusion of "pressing into" the page
- Transition duration: `0.1s` (snappy, responsive feel)

### Link Highlight Color

All link hovers change background to **Neon Green (#A8FF78)**:
```css
.links a:hover {
    background: #A8FF78;
}
```

**Exceptions:**
- Tor links: No background color change (grey remains)
- App links: No background color change (purple remains)

---

## 10. Design Tokens Summary

For quick reference, here are all design tokens in CSS custom property format:

```css
:root {
    /* Colors */
    --color-green: #A8FF78;
    --color-blue: #78D6FF;
    --color-purple: #D4ADFC;
    --color-yellow: #FDFFAB;
    --color-red: #FF6B6B;
    --color-cream: #FFF4E0;

    --color-black: #000000;
    --color-off-black: #1A1A2E;
    --color-dark-gray: #333333;
    --color-medium-gray: #444444;
    --color-gray: #666666;
    --color-pale-gray: #E8E8E8;
    --color-off-white: #F5F5F5;
    --color-white: #FFFFFF;

    /* Typography */
    --font-family: 'Space Grotesk', -apple-system, sans-serif;
    --font-family-mono: 'Courier New', monospace;
    --font-weight-semibold: 600;
    --font-weight-bold: 700;
    --line-height: 1.6;

    /* Shadows */
    --shadow-large: 6px 6px 0 #000;
    --shadow-medium: 4px 4px 0 #000;
    --shadow-small: 2px 2px 0 #000;
    --shadow-mobile-large: 4px 4px 0 #000;
    --shadow-mobile-medium: 3px 3px 0 #000;
    --shadow-mobile-small: 1px 1px 0 #000;

    /* Borders */
    --border-thick: 3px solid #000;
    --border-medium: 2px solid #000;
    --border-thin: 1.5px solid #000;
    --border-subtle: 1px solid #000;

    /* Spacing */
    --spacing-xs: 0.5rem;    /* 8px */
    --spacing-sm: 0.75rem;   /* 12px */
    --spacing-md: 1rem;      /* 16px */
    --spacing-lg: 1.5rem;    /* 24px */
    --spacing-xl: 2rem;      /* 32px */
    --spacing-2xl: 2.5rem;   /* 40px */

    /* Container */
    --container-max-width: 700px;

    /* Transitions */
    --transition-fast: 0.1s;
}
```

---

## 11. Implementation Guidelines

### For Frontend Developers

1. **Use CSS custom properties** for maintainability
2. **Maintain shadow consistency:** Always use hard shadows (no blur)
3. **Never add border-radius:** Sharp corners are essential to the aesthetic
4. **Preserve hover interactions:** Transform + shadow reduction creates the "press" effect
5. **Test on mobile:** Verify shadow sizes and spacing at <520px width
6. **Accessibility first:** Ensure contrast ratios meet WCAG AA minimum

### For Future Designers

1. **Add new colors sparingly:** The palette is intentionally limited
2. **Maintain the "bold" aesthetic:** Subtle gradients or soft shadows will clash
3. **Keep typography simple:** Space Grotesk at 600/700 weights is the signature
4. **Preserve playfulness:** Neo-brutalism should feel fun, not harsh
5. **Test with real content:** Long URLs and Tor addresses must remain readable

---

## 12. Psychological & Behavioral Analysis

### Design Psychology

**Neo-Brutalism User Perception:**
- **Trust through transparency:** The bold, unpretentious design signals authenticity
- **Memorability:** Distinctive aesthetic creates strong brand recall
- **Playfulness:** Reduces anxiety around security/safety topics
- **Clarity:** High contrast and simple hierarchy reduce cognitive load

**Color Psychology:**
- **Neon Green (#A8FF78):** Growth, safety, "go" action
- **Sky Blue (#78D6FF):** Trust, reliability, calm
- **Soft Purple (#D4ADFC):** Creativity, uniqueness
- **Cream Yellow (#FDFFAB):** Warmth, attention (not alarming)
- **Alert Red (#FF6B6B):** Urgency, danger (used sparingly for warnings)

**Behavioral Economics Principles:**
1. **Salience:** Bold colors and shadows draw attention to key actions
2. **Visual hierarchy:** Clear sectioning reduces decision fatigue
3. **Feedback:** Hover states provide immediate interaction confirmation
4. **Scarcity/urgency:** Warning section uses red to signal importance

### Cognitive Load Management

- **Chunking:** Information organized into clear sections (Browser, Tor, Apps, Warning)
- **Progressive disclosure:** Warning section separated to avoid alarm fatigue
- **Recognition over recall:** Color-coded tags (Auto, Backup) aid quick scanning
- **Fitts's Law:** Large touch targets on mobile reduce interaction error

---

## 13. File Structure & Assets

### Required Assets

1. **Font:** Space Grotesk (Google Fonts)
   - Weights: 400, 600, 700
   - Import: `https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap`

2. **Icons:** None currently used (text-only design)

3. **Images:** None currently used

### File Organization

```
/
├── index.html          (current monolithic file)
├── styles/
│   └── main.css        (future: extracted CSS)
├── assets/
│   └── fonts/          (future: self-hosted fonts)
└── 工作过程_20250405/
    └── 01_visual_style_guide.md (this document)
```

---

## 14. Future Recommendations

### Short-term Improvements

1. **Extract CSS:** Move styles to separate `.css` file for maintainability
2. **Add focus states:** Implement keyboard navigation support
3. **Contrast fixes:** Darken Alert Red and footer text for accessibility
4. **CSS custom properties:** Convert to design tokens for easier theming

### Long-term Enhancements

1. **Dark mode:** Develop alternative color scheme respecting neo-brutalism principles
2. **Animation library:** Create reusable transition/animation utilities
3. **Component library:** Extract buttons, cards, tags into reusable components
4. **Design token system:** Integrate with style dictionary for multi-platform use

### Brand Extensions

1. **Favicon:** Create bold, high-contrast icon matching the aesthetic
2. **Social sharing image:** Design OG image with same visual language
3. **Print stylesheet:** Adapt for high-contrast black & white printing

---

## Appendix: Quick Reference Card

### Most Used Values

```css
/* Colors */
background: #FFF4E0;        /* Page background */
background: #A8FF78;        /* Primary accent */
border: 3px solid #000;     /* Outer containers */
border: 2px solid #000;     /* Interactive elements */
box-shadow: 6px 6px 0 #000; /* Large shadow */
box-shadow: 4px 4px 0 #000; /* Medium shadow */

/* Typography */
font-family: 'Space Grotesk', -apple-system, sans-serif;
font-weight: 600;           /* Default text */
font-weight: 700;           /* Headings */
font-size: 2.6rem;          /* H1 */
font-size: 1.2rem;          /* H2 */
font-size: 1rem;            /* Body */

/* Spacing */
padding: 1.5rem;            /* Section padding */
gap: 0.75rem;               /* Grid gap */
max-width: 700px;           /* Container width */

/* Transitions */
transition: all 0.1s;       /* Hover transitions */
```

---

**Document End**

*This style guide is a living document. Update as the design evolves.*
