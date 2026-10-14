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
2. 找到檔案修改，直接存檔
   | 位置 | 檔案 | 內容 |
   |---|---|---|
   | `common\Language\`（**銑刀機種共用**） | `Cht.ini` / `Chs.ini` / `English.ini` / `Other_1.ini` / `Other_2.ini` | 介面文字、程式訊息 `[Get_Msg]`：繁中 / 簡中 / 英文 / 其他語言 |
   | `machines\<機種>\Language\` | `Message_Cht.ini` / `Message_Chs.ini` / `Message_Eng.ini` / `Message_Other_*.ini` | 編號訊息（`Msg_1`…）、警報、PLC 訊號 |
3. commit（訊息寫清楚改了什麼，例如 `GAM386AT 修正切割Y軸中文名稱`）→ push

> 銑刀機種的介面文字只有一份，改 `common\Language\` 就是全部一起改。
> 例外：**雷射機 GAM390 是獨立的產品線，不和銑刀機種共用**。`machines\GAM390\Language\` 放它自己完整的介面檔，部署時不使用 `common`；GAM390 的內容（例如訊息 290 以後、雷射專用表單）**不要補到銑刀機種**。
> 編號訊息檔是每個機種各一份。銑刀機種要改同一句話，就每個機種的檔案都改，一起 commit；新的訊息請改用 `[Get_Msg]`。

### 新增程式訊息（`[Get_Msg]`）
程式裡寫 `Get_Msg(L"確認復歸?")`，文字放在 `common\Language\` 5 個介面檔最後的 `[Get_Msg]` 段落，**銑刀機種共用，不用編號**：
```ini
; Cht.ini
[Get_Msg]
確認復歸?=確認復歸?
確認復歸? msg=確認復歸?\n若確認復歸請確認安全門......

; English.ini（Other_1.ini、Other_2.ini 同英文）
[Get_Msg]
確認復歸?=Confirm homing?
確認復歸? msg=Confirm homing?\nPlease make sure the safety door......
```
- 左邊是 key，就是程式裡寫的字；短句直接用原文，長句取一個好認的短名（例如加 ` msg`）
- **Cht.ini 一定要加**；其他語言還沒翻譯時，畫面會先顯示繁中，Cht.ini 也沒有時直接顯示 key
- key 不能有半形 `=`、不能用 `;` 或 `[` 開頭；前後空白不算；英文字母不分大小寫；換行寫成 `\n`
- 程式裡的 key 要和 ini 一字不差，打錯不會當掉，只會直接顯示 key
- 程式少了 `L`（`Get_Msg("確認復歸?")`）會編譯失敗，不會跑出亂碼
- GAM390（雷射）要用的話，加在它自己的 `machines\GAM390\Language\Cht.ini` 等檔案

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
會把共用的 `common\Language` 和該機種的 `Language`、`PLCIni` 複製到指定資料夾（exe 所在處）。機種資料夾裡有自己的 `Cht.ini`（GAM390）就是獨立機種，不複製 `common`。

### 開發時更新 bin 的語言檔
本 repo 和 Gam320 程式 repo **完全獨立**：Gam320 的 pull、切分支都不會動到語言檔，要拿新語言檔必須在這裡另外 `git pull`。
```
git pull
deploy.bat GAM300AT C:\Program1\GAM320AT\bin
```
> ⚠ deploy 會**覆蓋** bin 裡的語言檔。在 bin 裡改過的翻譯，請先改回本 repo 再 commit。
> 程式遇到新表單時會自動把該段文字寫進 bin 裡的 ini，這些內容要複製回本 repo 的 `common\Language\` 才會保留。

### 新增機種
複製一個最接近的機種資料夾，改名後修改內容，commit → push。銑刀機種的介面文字用 `common` 的，不用複製；不和銑刀共用的產品線（例如雷射），才在機種的 `Language\` 放自己完整的 `Cht.ini` 等檔案。

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
common/Language/           銑刀機種共用的介面語言檔，含程式訊息 [Get_Msg]（UTF-16 LE）
machines/<機種>/Language/  機種的編號訊息語言檔（UTF-16 LE）；GAM390（雷射）另有自己完整的介面語言檔
machines/<機種>/PLCIni/    PLC 參數（PLC.ini 等）與參數名稱（Name_*.ini，UTF-16 LE）
data/alarm-codes.csv       警報碼主檔（改這個）
docs/alarm-codes.md        自動產生，勿手改
tools/                     轉換、檢查腳本（GitHub 自動執行）
.github/workflows/         GitHub 自動檢查設定
deploy.bat                 部署到機台 / bin
```
