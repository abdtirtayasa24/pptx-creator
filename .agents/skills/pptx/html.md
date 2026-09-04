# Native Interactive HTML Presentations

Use this guide when the user requests `/pptx html`, `/skill:pptx html`, an interactive HTML deck, or an HTML presentation.

## Output Contract

Create a presentation as native HTML, CSS, and JavaScript.

- Output `.generated/<descriptive-name>.html` by default.
- Do not create `.pptx` or `.pdf` unless the user also requests them.
- Preserve every requested/source slide as one ordered 16:9 HTML slide.
- Rebuild slide content as DOM elements. Use SVG or canvas for charts.
- Never use rendered slide screenshots as slide backgrounds or full-slide `<img>` elements.
- Normal content images, illustrations, and logos are allowed.
- Prefer one self-contained HTML file. Embed local data and small required assets.

## Required Workflow

1. Inspect source files, slide order, tables, formulas, charts, branding, and notes.
2. Create a slide map: source page → HTML slide → layout → interaction.
3. Extract structured data rather than transcribing chart pixels.
4. Build a shared design system with CSS variables and reusable JS renderers.
5. Implement every slide with semantic HTML and native chart marks.
6. Add presentation navigation and content-appropriate interactions.
7. Validate content, structure, JavaScript, accessibility, and browser rendering.
8. Perform at least one visual fix-and-verify cycle.

## Slide Architecture

Declare the expected page count for validation, especially when JavaScript renders slides:

```html
<meta name="presentation-slide-count" content="26">
```

Use a stable slide model:

```html
<article class="slide" data-index="0" data-section="Overview">
  <header>...</header>
  <div class="slide-content">...</div>
  <footer>...</footer>
</article>
```

Recommended shell:

- Fixed toolbar for filters and view controls
- 16:9 presentation stage showing one active slide
- Optional details panel for takeaway and source
- Previous/next controls and progress indicator
- Overview grid containing all slides

Use responsive scaling with `aspect-ratio: 16 / 9`, container query units, or a calculated transform. Provide print CSS with one slide per printed page.

## Native Content Rules

- Text must remain selectable and searchable.
- Tables must be real `<table>` elements.
- Charts must be SVG/canvas/DOM, not chart screenshots.
- Use structured source data for every visual and tooltip.
- Treat workbook, document, and model-generated strings as untrusted: HTML-escape them before DOM insertion.
- Do not pass source content to `eval()`, event-handler attributes, or unsanitized `innerHTML`.
- Keep slide titles, key metrics, source labels, and ordering faithful to the source.
- Add concise key takeaways when the source supports them; do not invent unsupported claims.

## Interaction Baseline

Include these unless the user opts out:

- Previous/next buttons
- Left/right and Page Up/Page Down keyboard navigation
- Home/End navigation
- Touch swipe navigation
- Slide progress and page count
- Fullscreen mode
- Overview/grid mode
- Search or section filtering for longer decks
- Hover and keyboard-focus states
- Tooltips on chart marks and meaningful data regions

Add data-specific filters when useful, such as month, segment, scenario, product, or geography. Filters must update native charts, KPIs, takeaways, and focused tables consistently.

## Charts

Use SVG by default for portable, dependency-free output.

- Give each point, bar, segment, or funnel stage a `<title>` or accessible tooltip.
- Make interactive marks keyboard focusable with `tabindex="0"`.
- Highlight the selected filter period without hiding historical context unless density requires it.
- Keep axes, legends, and labels readable at normal presentation size.
- Do not encode meaning by color alone; include labels or patterns.

## Tables and Dense Slides

Readability overrides literal compression.

- Target at least 11–12 CSS pixels at normal desktop presentation size.
- Use sticky headers, row hover/focus, and sufficient cell padding.
- Never shrink a large table until all rows barely fit.
- If a table is dense, use the relevant global filter to show a focused subset.
- Preserve access to all source rows through filters, tabs, drill-down, scrolling, or a detail view.
- Do not split a logical table across presentation pages unless the user permits it.
- Explain focused views with visible copy such as “Showing August; use the month filter for other periods.”

## Accessibility and Responsiveness

- Use semantic headings in order.
- Label controls with visible labels or `aria-label`.
- Support keyboard interaction for every control and tooltip target.
- Provide visible `:focus-visible` states.
- Respect `prefers-reduced-motion`.
- Ensure text and controls meet WCAG AA contrast.
- Test desktop and compact layouts; controls must not force horizontal overflow.
- On small screens, keep slides fully visible and move secondary controls into overview/details modes.

## Validation

Run the bundled structural validator:

```bash
python scripts/validate_html_presentation.py .generated/deck.html --min-slides 1
```

Extract inline JavaScript and syntax-check it when Node is available:

```bash
node --check generated-script.js
```

Render representative pages in a browser at desktop and compact sizes. Inspect at minimum:

- Cover and closing slides
- One chart-heavy slide
- One dense table slide
- One filtered state
- Overview mode

Check for overlap, clipping, unreadable text, broken tooltips, missing slides, filter inconsistencies, keyboard traps, horizontal overflow, and console errors.

## Completion Checklist

- [ ] Output is `.html`, not `.pptx`/`.pdf`
- [ ] Every source slide has a native HTML slide
- [ ] No rendered slide screenshots are used
- [ ] Text and tables are selectable
- [ ] Charts have interactive native marks
- [ ] Navigation, overview, and filters work
- [ ] Dense tables remain readable and fully accessible
- [ ] Desktop and compact browser QA completed
- [ ] At least one fix-and-verify cycle completed
