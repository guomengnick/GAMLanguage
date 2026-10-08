@echo off
chcp 65001 >nul
rem 用法: deploy.bat 機種 目標資料夾(exe 所在處)
rem 例:   deploy.bat GAM386AT D:\Release\GAM386AT
if "%~2"=="" ( echo 用法: deploy.bat 機種 目標資料夾 & exit /b 1 )
if not exist "%~dp0machines\%~1" ( echo 找不到機種 %~1 & exit /b 1 )
xcopy /E /I /Y "%~dp0machines\%~1\Language" "%~2\Language" >nul
xcopy /E /I /Y "%~dp0machines\%~1\PLCIni"   "%~2\PLCIni"   >nul
echo 已部署 %~1 語言檔到 %~2
