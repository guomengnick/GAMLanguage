@echo off
chcp 65001 >nul
rem clone 之後執行一次：啟用 tools\hooks 內的自動化
git config core.hooksPath tools/hooks
echo 已啟用 hook (CSV 修改後 commit 會自動更新 docs\*.md)
pause
