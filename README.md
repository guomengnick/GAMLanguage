# GAM-Language

全機種語言檔與警報碼。**永遠使用最新版**，舊機台使用新語言包可相容。

## 第一次使用
```
git clone <repo網址> C:\Program1\GAM320AT\Language
cd C:\Program1\GAM320AT\Language
setup.bat
```

## 日常
| 要做的事 | 怎麼做 |
|---|---|
| 拿最新語言檔 | `git pull` |
| 改翻譯 | 直接改 `machines/<機種>/Language/*.ini` → commit → push |
| 改警報碼 | 用 Excel 開 `data/alarm-codes.csv` 修改存檔 → commit（MD 自動更新）→ push |
| 查警報碼 | 在 GitHub 上看 [docs/alarm-codes.md](docs/alarm-codes.md) |
| 部署到機台 | `deploy.bat GAM386AT D:\Release\GAM386AT` |

## 結構
```
machines/<機種>/Language/  介面與訊息語言檔 (UTF-16)
machines/<機種>/PLCIni/    PLC 參數與名稱
data/alarm-codes.csv       警報碼主檔（改這個）
docs/alarm-codes.md        自動產生，勿手改
tools/                     轉換腳本與 git hook
```

## 注意
- ini 是 UTF-16，`.gitattributes` 已處理，GitHub 上 diff 看得到中文；**請勿刪改 .gitattributes**。
- 原 `Backup\日期` 資料夾已轉為 git 歷史（GAM300AT 2020-10-08 起），不再需要手動備份。
