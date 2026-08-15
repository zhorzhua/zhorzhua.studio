# zhorzhua.studio

One-page site of Zhorzhua Studio. Static: `index.html` + `linen.svg` + `icons/`. No build.

- Visual canon: warm brown-black woven wall, fine irregular linen + grain, matte glass cells, letterpress text. There is no global top lamp.
- Current light behavior: a quiet glow is always centred behind each glass cell; hover makes it flare on pointer devices, while on touch screens the cell nearest the middle of the screen gets the stronger light as the page scrolls. The real `.spot` remains a sibling behind the glass, never a pseudo-element inside its backdrop-filter stacking context.
- The glow fades fully before its oversized box edge, so it can leave the panel without exposing a rectangular boundary. Every light transition is gated by reduced-motion.
- `linen.svg` and the fine grain share one full-page layer, so the material stays even from the hero through the footer without the 3px scanline aliasing of the earlier CSS weave.
- Statuses are honest; `.store` button only with a real App Store URL.
- Privacy links to the live HATOB page on zhorzhua.github.io (Support URL of the app under review — do not touch that repo's root).

Publish: GitHub Pages from `main` of `zhorzhua/zhorzhua.studio`, then a `CNAME` file with `zhorzhua.studio` once the domain is bought.

Local look: `python3 -m http.server 8811` in this folder.

Share/meta: `og.jpg` (1200×630, rendered from the hero), `apple-touch-icon.png` and `favicon.png` (the lamp). `og:image` is an absolute URL — update it when the domain moves to `zhorzhua.studio`.
