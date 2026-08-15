# zhorzhua.studio

One-page site of Zhorzhua Studio. Static: `index.html` + `icons/`. No build.

- Visual canon: Fable, AI Room FABLE-ROOM-038 (v6.3) — glass cells, lamp at the top of the page, linen + grain, letterpress text.
- v6.4 (Asya): the lamp spot is a real element *behind* the glass (`.spot` sibling, not a pseudo inside the backdrop-filter stacking context); glass alphas lowered to matte; on touch screens the cell nearest the middle of the screen is lit (no hover there); reduced-motion honoured.
- Statuses are honest; `.store` button only with a real App Store URL.
- Privacy links to the live HATOB page on zhorzhua.github.io (Support URL of the app under review — do not touch that repo's root).

Publish: GitHub Pages from `main` of `zhorzhua/zhorzhua.studio`, then a `CNAME` file with `zhorzhua.studio` once the domain is bought.

Local look: `python3 -m http.server 8811` in this folder.
