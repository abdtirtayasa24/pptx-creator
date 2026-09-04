# Slide theme catalog

Seventeen themes. Pick one, then load **only** `themes/<id>/theme.json` (and `theme.css` for the HTML path). Never load more than one theme per run.

## Light-ground themes

| id | Feel | Type pairing | Ground | Accent | Reach for it when |
|---|---|---|---|---|---|
| **blush** | Clean, quiet, safe | Montserrat / Roboto | White + blush `#FFF8F8` | Coral `#FF5252` | SaaS, startups, sales and onboarding. The default when nothing else fits. |
| **meridian** | Institutional, restrained | Manrope / Source Sans 3 | White + slate `#F4F6F8` | Copper `#C77B30` | Board and investor decks, annual reports, policy briefings. Dense tables and financial data. |
| **marmalade** | Warm, rounded, friendly | Fredoka / Onest | White + cream `#FFF3E0` | Orange `#F8721F` | Consumer, education, community. Approachable, not corporate. |
| **crayon** | Bright, playful, childlike | Jost / Nunito / Bubblegum Sans | White + peach `#FFF0E5` | Orange `#F7941E` + teal | Education, childcare, non-profit, culture decks. Meant to feel joyful. |
| **aurora** | Soft, polished, gradient | Lexend Deca / Jost | Off-white `#F9FBFF` | Coral → indigo gradient | Portfolios, creative pitches, founder decks. |
| **spectrum** | Bold geometric, high energy | Poppins | White + pale blue `#F5F7FC` | Violet `#6A45FF` + 6 hues | Many parallel categories that each need a colour. Launches, agency work. |
| **foundry** | Condensed uppercase, industrial | Oswald / Rubik | White + `#F1F1F1` | Electric green `#08D665` | Sports, fitness, construction, events. Confident and physical. |
| **broadsheet** | Editorial print, serif | Fraunces / Inter | Paper `#FAF7F2` | Clay red `#B3402E` | Long-form narrative, research findings, keynotes. Pull quotes that land like a magazine spread. |
| **clay** | Earthy, tactile, organic | Bricolage Grotesque / Karla | Sand `#F2EBE0` | Terracotta `#B5623C` + moss | Sustainability, craft and food brands, B-Corp reporting. Handmade, not manufactured. |
| **linen** | Calm, airy, pastel | Outfit / DM Sans | Warm off-white `#F7F5F2` | Sage `#7FA692` + blush | Healthcare, mindfulness, HR and people decks, retrospectives. Lowers the room's temperature. |
| **vellum** | Editorial, premium, literary | Playfair Display / Source Sans 3 | Parchment `#FBF7EE` | Ochre `#D79A2B` + oxblood | Reports, strategy narratives, cultural institutions, premium services. |
| **lagoon** | Calm, scientific, humane | Manrope / IBM Plex Sans | Mist aqua `#F2FBFA` | Teal `#00A6A0` + blue | Healthcare, climate, research, analytics and evidence-heavy decks. |
| **blueprint** | Precise, technical, systematic | Space Grotesk / IBM Plex Sans / IBM Plex Mono | Pale blue grid `#F6F8FF` | Cobalt `#2F6BFF` + cyan | Engineering, product architecture, roadmaps, developer tooling and systems. |
| **grove** | Grounded, organic, human | DM Sans / Noto Sans | Warm sage-white `#F7F7F0` | Clay `#C9673B` + forest | Sustainability, social impact, food, wellness and mission-driven organizations. |
| **workbench** | Retro maker, tactile, inventive | Bricolage Grotesque / IBM Plex Mono | Butter `#FFF8D6` | Vermilion `#E94F37` + teal | Workshops, hackathons, innovation labs, creative tech and maker communities. |

## Dark-ground themes

| id | Feel | Type pairing | Ground | Accent | Reach for it when |
|---|---|---|---|---|---|
| **obsidian** | Dark minimal, elegant | Inter / General Sans | Near-black `#13111A` | Tangerine `#FFB646` | Investor decks, product architecture. Presented in a dark room or on a big screen. |
| **terminal** | Developer dark, bento | Space Grotesk / Inter / JetBrains Mono | `#0D1117` | Neon green `#7DF9A6` | Engineering reviews, API and infra decks, technical demos. The audience reads code. |

## Quick selection rules

Walk these in order and stop at the first match.

1. **Audience needs code, API, or infrastructure detail on a dark ground?** → `terminal`.
2. **Dark room or large-screen keynote, non-technical?** → `obsidian`.
3. **Financial tables, board, or regulator?** → `meridian`. Its smaller scale, hairline rules, and restrained accent support dense data.
4. **More than four parallel data categories?** → `spectrum`. Its six-colour series emphasizes category separation.
5. **Technical system, product architecture, roadmap, or developer tooling on a light ground?** → `blueprint`.
6. **Scientific, healthcare, climate, analytics, or evidence-heavy?** → `lagoon`.
7. **Premium strategy narrative, cultural institution, or literary editorial tone?** → `vellum`.
8. **Research story, keynote narrative, or hero pull quote with a newspaper feel?** → `broadsheet`.
9. **Workshop, hackathon, innovation lab, or creative-tech facilitation?** → `workbench`.
10. **Children, parents, or students?** → `crayon`.
11. **Sustainability, craft, or food that must feel tactile and handmade?** → `clay`.
12. **Mission-driven sustainability, social impact, food, or wellness story?** → `grove`.
13. **Healthcare, mindfulness, HR, or a difficult retrospective?** → `linen`.
14. **Loud and physical?** → `foundry`.
15. **Personal portfolio or creative pitch?** → `aurora`.
16. **Warm consumer or community?** → `marmalade`.
17. **Nothing in the brief suggests a direction?** → `blush`.

## Coverage map

| Axis | Range covered |
|---|---|
| Ground | 15 light, 2 dark |
| Type | Serif-led: broadsheet, vellum · Monospace roles: terminal, blueprint, workbench · Sans-led: the remaining themes |
| Temperature | Warm: marmalade, crayon, clay, broadsheet, blush, vellum, grove, workbench · Cool: meridian, aurora, linen, terminal, lagoon, blueprint · Neutral: spectrum, foundry, obsidian |
| Energy | Loud: foundry, spectrum, crayon, workbench · Measured: meridian, broadsheet, obsidian, blush, vellum, blueprint · Quiet: linen, clay, aurora, marmalade, terminal, lagoon, grove |
| Density | Dense (21–23px body): meridian, terminal, foundry, blush, vellum, lagoon, blueprint, grove, workbench · Roomy (24–25px body): aurora, linen, marmalade, crayon, clay, broadsheet, spectrum, obsidian |
| Corners | Square (0–6px): broadsheet, meridian, foundry, vellum, blueprint, workbench · Soft (10–18px): spectrum, aurora, obsidian, blush, terminal, lagoon · Round (20–28px): clay, linen, marmalade, crayon, grove |

## What every theme guarantees

- 1280×720 canvas, 64px safe inset
- Every `surface` / `on` pair clears 4.5:1 — measured, and stored in `contrast`
- `accent.onLight` and `accent.onDark` are pre-shifted text-safe variants, both ≥4.5:1. **Never set small text in `accent.primary`**
- Six-colour `series` for charts, all distinct within the theme
- Identical core key set across all seventeen, so switching is a one-line change

See `SCHEMA.md` for the full key list.