---
description: Create a PPTX deck or native interactive HTML presentation
argument-hint: "<html|pptx> <instructions>"
---
Use the project PPTX skill at `.agents/skills/pptx/SKILL.md`.

Requested mode: `$1`

- If the mode is `html`, read `.agents/skills/pptx/html.md` completely and create a native interactive HTML slide presentation instead of `.pptx` or `.pdf`.
- The HTML must recreate every slide with selectable HTML text, semantic tables, and native SVG/canvas/DOM charts. Never use rendered slide screenshots as full-slide images.
- If the mode is `pptx`, or any value other than `html`, follow the standard PPTX workflow.

User instructions:
${@:2}
