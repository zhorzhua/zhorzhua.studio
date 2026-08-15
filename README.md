# zhorzhua.studio

One-page site of Zhorzhua Studio. Static: `index.html` + `icons/`. No build.

- Visual canon: warm brown-black wall, fine stippled dots + grain, matte glass cells, letterpress text. There is no global top lamp and no fabric weave.
- Current light behavior: the original soft centred underlight sits behind each glass cell and grows on pointer hover; on touch screens the cell nearest the middle of the screen gets the stronger light as the page scrolls.
- The newer substrate treatment remains underneath it: a slightly app-tinted, asymmetric bounce appears through brighter stipple below and beside the active card. The intended combination is the original smooth panel glow plus this restrained path-traced wall response.
- The smaller fine dots and stochastic grain share one full-page layer, so the material stays even from the hero through the footer without directional threads or the 3px scanline aliasing of the earlier CSS weave.
- Statuses are honest; `.store` button only with a real App Store URL.
- Privacy links to the live HATOB page on zhorzhua.github.io (Support URL of the app under review — do not touch that repo's root).

Publish: GitHub Pages from `main` of `zhorzhua/zhorzhua.studio`, then a `CNAME` file with `zhorzhua.studio` once the domain is bought.

Local look: `python3 -m http.server 8811` in this folder.

Share/meta: `og.jpg` (1200×630, rendered from the hero), `apple-touch-icon.png` and `favicon.png` (the lamp). `og:image` is an absolute URL — update it when the domain moves to `zhorzhua.studio`.
