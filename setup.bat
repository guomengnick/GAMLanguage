@echo off
chcp 65001 >nul
rem clone 之後執行一次：啟用 tools\hooks 內的自動化
git config core.hooksPath tools/hooks
echo 已啟用自動檢查：commit 時檢查語言檔編碼、CSV 修改後自動更新 docs\*.md
pause
