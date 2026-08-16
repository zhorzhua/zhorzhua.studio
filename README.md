# zhorzhua.studio

One-page site of Zhorzhua Studio. Static: `index.html` + `icons/`. No build.

- Visual canon: dark graphite wall, fine stippled dots + grain, matte glass cells, letterpress text. Warmth lives inside the app cards; there is no global top lamp and no fabric weave.
- Current light behavior: a quiet glow is clipped inside each glass cell; hover strengthens it on pointer devices, while on touch screens the cell nearest the middle of the screen gets the stronger internal light as the page scrolls.
- Outside the panel there is no glow or app-tinted response: the graphite wall remains visually uninterrupted. The internal light uses no blur, avoiding colour banding/posterization on 8-bit displays.
- The smaller fine dots and stochastic grain share one full-page layer, so the material stays even from the hero through the footer without directional threads or the 3px scanline aliasing of the earlier CSS weave.
- Statuses are honest; `.store` button only with a real App Store URL.
- Privacy links to the live HATOB page on zhorzhua.github.io (Support URL of the app under review — do not touch that repo's root).

Publish: GitHub Pages from `main` of `zhorzhua/zhorzhua.studio`, with `CNAME` set to `zhorzhua.studio` and DNS managed by Cloudflare.

Local look: `python3 -m http.server 8811` in this folder.

Share/meta: `og.jpg` (1200×630, rendered from the hero), `site-mark.svg`, `apple-touch-icon.png` and `favicon.png` (the studio monogram). Canonical and Open Graph URLs use `https://zhorzhua.studio/`.
