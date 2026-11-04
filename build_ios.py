"""由 Android 版的 web/index.html 產生 iPhone 可安裝的網頁 App（PWA）index.html。"""
import sys, pathlib
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
head_add = """<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="鏡映拼圖">
<meta name="format-detection" content="telephone=no">
"""
sw = """<script>if ('serviceWorker' in navigator) addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));</script>
"""
assert '<meta charset="utf-8">' in src and '</body>' in src
out = src.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n' + head_add, 1).replace('</body>', sw + '</body>', 1)
pathlib.Path(sys.argv[2]).write_text(out, encoding="utf-8")
print("wrote", sys.argv[2], len(out))
