# 鏡映拼圖 — iPhone／iPad 版 v1.2.0

iPhone 版是「網頁 App」（PWA）：放在 GitHub Pages 上，用 Safari「加入主畫面」後，
桌面會出現萬花筒圖示，點開為全螢幕 App，第一次開啟後沒有網路也能使用。
不需要 App Store、不需要 Apple 開發者帳號，也沒有 7 天到期的問題。

## 一、放上 GitHub Pages（只需做一次）

1. 到 github.com/new 建立儲存庫，名稱 `mirror-collage-ios`，選 **Public**
   （GitHub 免費帳號的 Pages 只支援公開儲存庫）。
2. 「uploading an existing file」→ 拖入本資料夾全部檔案 → Commit changes。
3. Settings → Pages → Source 選「Deploy from a branch」，Branch 選 `main`、`/(root)` → Save。
4. 約 1 分鐘後網址為 `https://jychen33.github.io/mirror-collage-ios/`。

## 二、在 iPhone 安裝

1. 用 **Safari** 開啟上面的網址（必須是 Safari）。
2. 點下方「分享」按鈕 →「加入主畫面」→「新增」。
3. 主畫面出現「鏡映拼圖」圖示，之後從圖示開啟即可。

## 儲存作品

按「儲存」會開啟分享選單，選「儲存影像」即存到「照片」。

## 更新

改版後把新的 `index.html` 上傳到同一個儲存庫即可；iPhone 下次連網開啟時自動更新。
若要強制更新，可修改 `sw.js` 第 2 行的版本字串。

## 檔案

| 檔案 | 用途 |
|---|---|
| index.html | 主程式（由 Android 版 web/index.html 經 build_ios.py 產生） |
| manifest.webmanifest | App 名稱、圖示、全螢幕設定 |
| sw.js | 離線快取 |
| icon-180/192/512.png | 主畫面圖示 |
| .nojekyll | 讓 GitHub Pages 原樣提供檔案 |

© 2026 James Chen 陳進勇 版權所有
