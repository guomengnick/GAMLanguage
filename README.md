# GAMLanguage

全機種語言檔與警報碼。**永遠使用最新版**，舊機台用新語言包可相容。
每個人都可以自己更新、修改，不需要再請專人統一處理；誰改了什麼，git 都有紀錄。

---

## 一、第一次使用（每台電腦做一次）

只要下載一次，沒有其他設定：
```
git clone https://github.com/guomengnick/GAMLanguage.git C:\Program1\GAM320AT\GAMLanguage
```
> 用 GitHub Desktop、TortoiseGit 等工具 clone 也可以。以下指令都在這個資料夾裡執行。

---

## 二、日常操作

### 拿最新語言檔
```
git pull
```
**修改任何檔案之前，先 pull 一次**，可以避免和別人改到同一處而衝突。

### 改翻譯（介面、訊息）
1. `git pull`
2. 打開 `machines\<機種>\Language\` 裡的檔案修改，直接存檔
   | 檔案 | 內容 |
   |---|---|
   | `Cht.ini` / `Chs.ini` / `English.ini` | 介面文字：繁中 / 簡中 / 英文 |
   | `Message_Cht.ini` / `Message_Chs.ini` / `Message_Eng.ini` | 訊息文字 |
   | `Other_1.ini` / `Other_2.ini`、`Message_Other_*.ini` | 其他語言 |
3. commit（訊息寫清楚改了什麼，例如 `GAM386AT 修正切割Y軸中文名稱`）→ push

> 一次只改需要的機種。多個機種要改同一句話，就每個機種的檔案都改，一起 commit。

### 改 PLC 參數名稱
`machines\<機種>\PLCIni\Name_TW.ini` / `Name_CN.ini` / `Name_EN.ini`，流程同上。

### 改警報碼
1. `git pull`
2. 用 Excel 開 `data\alarm-codes.csv` 修改
3. 存檔時選 **「CSV UTF-8（逗號分隔）」**
4. commit → push
5. 約 1 分鐘後，GitHub 會自動多一筆「由 CSV 自動更新 MD」的 commit（`docs\alarm-codes.md`），不用管它，下次記得先 `git pull`

### 查警報碼
直接在 GitHub 上看 **[docs/alarm-codes.md](docs/alarm-codes.md)**，可用 Ctrl+F 搜尋。

### 部署到機台 / 出貨
```
deploy.bat GAM386AT D:\Release\GAM386AT
```
會把該機種的 `Language`、`PLCIni` 複製到指定資料夾（exe 所在處）。

### 開發時更新 bin 的語言檔
本 repo 和 Gam320 程式 repo **完全獨立**：Gam320 的 pull、切分支都不會動到語言檔，要拿新語言檔必須在這裡另外 `git pull`。
```
git pull
deploy.bat GAM300AT C:\Program1\GAM320AT\bin
```
> ⚠ deploy 會**覆蓋** bin 裡的語言檔。在 bin 裡改過的翻譯，請先改回本 repo 再 commit。
> 程式遇到新表單時會自動把該段文字寫進 bin 裡的 ini，這些內容要複製回本 repo 才會保留。

### 新增機種
複製一個最接近的機種資料夾，改名後修改內容，commit → push。

### 查誰改過某個檔案
GitHub 上打開該檔案 → 右上角 **History**；或按 **Blame** 看每一行是誰改的。

---

## 三、⚠ 注意事項

| 不要做 | 原因 |
|---|---|
| 把 ini **另存成 UTF-8 或 ANSI** | 語言檔必須是 **UTF-16 LE**，存錯整個檔案會變亂碼。直接修改後存檔不會改變編碼（記事本、Notepad++、VS Code 都可以），只有「另存新檔」時要注意編碼 |
| 手改 `docs\*.md` | 它是由 CSV 自動產生的，改 CSV 就好 |
| 修改或刪除 `.gitattributes` | 它負責 UTF-16 轉換，刪掉之後 diff 會看不到中文 |
| 再建 `Backup\日期` 資料夾 | git 就是備份，所有舊版本都可以從 History 找回 |
| 把 Excel 存成一般 CSV | 會變成 Big5，中文亂碼 |

### GitHub 自動檢查
每次 push 後，GitHub 會自動（約 1 分鐘）：
1. 檢查所有語言檔編碼 → 有問題時該 commit 顯示**紅色 ✗**，點進去可看到是哪個檔案
2. 警報碼 CSV 有改 → 自動產生 MD 並 commit

push 後到 GitHub 首頁看一下 commit 旁邊是綠色 ✓ 就好。

---

## 四、常見問題

**Q：GitHub 顯示紅色 ✗「語言檔編碼錯誤，必須存成 UTF-16 LE」**
該檔案在 git 裡已經變亂碼，要從原始內容修復：
1. 從自己電腦的備份或 bin 裡找回該檔案正確的內容
2. 用記事本打開 → 另存新檔 → 編碼選「UTF-16 LE」→ 覆蓋 repo 裡的檔案
3. commit → push，確認變回綠色 ✓

不確定怎麼處理時，**先不要再改其他東西**，請熟 git 的同事協助（可用 `git revert` 回到上一版）。

**Q：pull 時出現衝突（conflict）**
代表你和別人改到同一行。打開檔案找 `<<<<<<<` 標記，保留正確的內容並刪除標記，存檔後 commit。不確定的話先找改的人討論。

**Q：改錯了想還原**
還沒 commit：`git checkout -- 檔案路徑`
已經 push：在 GitHub History 找到該 commit，`git revert <commit編號>` 後 push。

**Q：想看某個檔案以前的版本**
GitHub 上打開該檔案 → History → 點選要看的 commit。GAM300AT 的歷史可以追溯到 2020-10-08。

---

## 結構
```
machines/<機種>/Language/  介面與訊息語言檔（UTF-16 LE）
machines/<機種>/PLCIni/    PLC 參數（PLC.ini 等）與參數名稱（Name_*.ini，UTF-16 LE）
data/alarm-codes.csv       警報碼主檔（改這個）
docs/alarm-codes.md        自動產生，勿手改
tools/                     轉換、檢查腳本（GitHub 自動執行）
.github/workflows/         GitHub 自動檢查設定
deploy.bat                 部署到機台 / bin
```
