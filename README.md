# zhorzhua.studio

One-page site of Zhorzhua Studio. Static: `index.html`, `icons/`, and image assets. No build.

- Visual direction: pure black background (`#000000`), matte glass cells, and letterpress text. The background is flat, with no texture or grain. Light stays warm inside the app cards; there is no global top lamp.
- Current light behavior: a quiet glow is clipped inside each glass cell; hover strengthens it on pointer devices, while on touch screens the cell nearest the middle of the screen gets the stronger internal light as the page scrolls.
- Outside the panel there is no glow or app-tinted response. The internal light uses no blur; the wall has no large CSS gradient that could introduce colour banding/posterization.
- The existing linen and grain assets are retained but are not displayed.
- Statuses are honest; `.store` button only with a real App Store URL.
- Privacy links to the live Hatob page on zhorzhua.github.io (Support URL of the app under review — do not touch that repo's root).

Publish: GitHub Pages from `main` of `zhorzhua/zhorzhua.studio`, with `CNAME` set to `zhorzhua.studio` and DNS managed by Cloudflare.

Local look: `python3 -m http.server 8811` in this folder.

Rebuild the linen only when changing its design: `python3 scripts/generate_linen.py` (NumPy and Pillow). The generated PNG is checked in; the website has no runtime or build dependency on Python. Keep this texture at its fixed CSS size instead of stretching it to cover the viewport.

Share/meta: `og.jpg` (1200×630, rendered from the hero), `site-mark.svg`, `apple-touch-icon.png` and `favicon.png` (the studio monogram). Canonical and Open Graph URLs use `https://zhorzhua.studio/`.

Safari touch icon: `apple-touch-icon-180-v5.png`, explicitly declared at 180 x 180. Both it and the root fallback `apple-touch-icon.png` are opaque RGB PNGs with the background reaching every edge. When refreshing a previously saved icon, change the linked filename as well as its contents; saved favourites may retain their previous image until Safari refreshes it.
