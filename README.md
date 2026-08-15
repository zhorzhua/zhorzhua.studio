# zhorzhua.studio

One-page site of Zhorzhua Studio. Static: `index.html` + `icons/`. No build.

- Visual canon: Fable, AI Room FABLE-ROOM-038 (v6.3) — glass cells, lamp at the top of the page, linen + grain, letterpress text.
- Current light behavior: a quiet glow is always centred behind each glass cell; hover makes it flare on pointer devices, while on touch screens the cell nearest the middle of the screen gets the stronger light as the page scrolls. The real `.spot` remains a sibling behind the glass, never a pseudo-element inside its backdrop-filter stacking context.
- Glass alphas are lowered to matte; the lamp remains absolute at the top and is capped at 1200px so it cannot create empty scroll after the footer; every light transition is gated by reduced-motion.
- Grain is a single full-page layer, separate from the lamp, so its texture stays even from the hero through the footer.
- Statuses are honest; `.store` button only with a real App Store URL.
- Privacy links to the live HATOB page on zhorzhua.github.io (Support URL of the app under review — do not touch that repo's root).

Publish: GitHub Pages from `main` of `zhorzhua/zhorzhua.studio`, then a `CNAME` file with `zhorzhua.studio` once the domain is bought.

Local look: `python3 -m http.server 8811` in this folder.

Share/meta: `og.jpg` (1200×630, rendered from the hero), `apple-touch-icon.png` and `favicon.png` (the lamp). `og:image` is an absolute URL — update it when the domain moves to `zhorzhua.studio`.
