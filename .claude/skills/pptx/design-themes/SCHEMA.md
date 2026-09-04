# Slide theme schema v1.0

Every `themes/<id>/theme.json` has exactly these keys. Same names, same shapes, seventeen themes. Swapping a theme should never require touching layout code.

## Canvas

```json
"canvas": { "w": 1280, "h": 720, "aspect": "16:9", "safeInset": 64, "unit": "px", "ptFactor": 0.75 }
```

Fixed canvas, no breakpoints. 1280×720 px is exactly 13.333in × 7.5in at 96 dpi, so **`pt = px × 0.75`** converts any value for python-pptx. Keep all content inside the 64px inset.

## Colour

| Key | Use |
|---|---|
| `surface.base` | Default slide background |
| `surface.alt` | Alternating / card background |
| `surface.brand` | Full-bleed brand slide |
| `surface.dark` | Dark section divider |
| `on.<name>` | The text colour to use **on** that surface. Never pick your own. |
| `contrast.<name>` | Measured ratio of the pair. All ≥ 4.5. |
| `accent.primary` | Fills only — bars, icons, shapes, large blocks |
| `accent.secondary` | Second fill |
| `accent.onLight` | Accent **as text** on light surfaces (pre-darkened to ≥4.5:1) |
| `accent.onDark` | Accent **as text** on dark surfaces (pre-lightened to ≥4.5:1) |

On the two `darkFirst` themes (`obsidian`, `terminal`) `surface.base` is dark, so `accent.onLight` is measured against `lightSurface`, not `surface.base`.
| `series[6]` | Chart categories, in order |
| `muted` | Secondary text, axis labels |
| `hairline` | Rules, borders, gridlines |
| `gradient` | Present on `aurora` only |

**The one rule that matters:** `accent.primary` is a fill, not a text colour. Bright brand hues fail contrast as small text on white — every one of these themes fails at 1.9–3.2:1. Use `accent.onLight` / `accent.onDark` for kickers, labels, and stat figures.

## Type

```json
"font": {
  "display": { "family", "stack", "weight", "tracking", "leading", "transform"? },
  "body":    { ... },
  "kicker":  { ... }
}
"fontUrl": ["https://..."]
```

Three roles only. `display` covers title-slide, slide-title and section-title; `body` covers everything readable; `kicker` is the small label above a title.

```json
"scale": { "display", "slideTitle", "sectionTitle", "lead", "body", "bodySm", "caption", "kicker" }
```

All px against the 1280×720 canvas. Sizes are re-based for projection, not carried over from the web source — `body` sits at 23–25px (≈18pt), not 16px.

## Everything else

| Key | Notes |
|---|---|
| `radius.card / chip / image` | px |
| `shadow.card / raised` | Full CSS shadow strings |
| `spacing` | `unit` 8, `gutter` 32, `blockGap` 24, `listGap` 16, `titleGap` 32 |
| `chart` | `grid`, `axis`, `label`, `series` — pre-resolved so charts need no lookups |
| `signature` | One sentence naming the theme's distinctive device. Apply it on the title slide and section dividers; don't repeat it on every slide. |
| `pptx` | `slideWidthIn`, `slideHeightIn`, font family names, `sizesPt` (the scale pre-converted) |
| `darkFirst` | Present and `true` on `obsidian` and `terminal`. Their `surface.base` is dark; `lightSurface` gives the inverse ground. |
| `fontNote` | Present where the source font was commercial or self-hosted |

## CSS classes shipped in `theme.css`

`.slide` `.slide--alt` `.slide--brand` `.slide--dark` · `.kicker` `.display` `.title` `.section-title` `.lead` `.caption` `.measure` · `.grid --2/--3/--4` · `.card` `.card--flat` · `.chip` `.rule` `.stat`

Dark-ground overrides are already wired: inside `.slide--dark`, kickers and stats switch to `accent.onDark` and cards go translucent. You do not need to handle that in generated markup.

## Fonts

Sixteen themes load entirely from Google Fonts. `obsidian` additionally loads General Sans from Fontshare. `spectrum` substitutes Poppins for the source theme's commercial Gordita — the stack tries Gordita first if licensed.

For the **pptx** path, fonts must be installed on the machine. If they aren't, python-pptx will silently substitute; fall back to the last entry in the stack instead.