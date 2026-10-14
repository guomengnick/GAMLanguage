@echo off
chcp 65001 >nul
rem 用法: deploy.bat 機種 目標資料夾(exe 所在處)
rem 例:   deploy.bat GAM386AT D:\Release\GAM386AT
if "%~2"=="" ( echo 用法: deploy.bat 機種 目標資料夾 & exit /b 1 )
if not exist "%~dp0machines\%~1" ( echo 找不到機種 %~1 & exit /b 1 )
rem 機種有自己的 Cht.ini = 獨立機種（例如雷射 GAM390），不使用共用的介面語言檔
if not exist "%~dp0machines\%~1\Language\Cht.ini" xcopy /E /I /Y /R "%~dp0common\Language" "%~2\Language" >nul
xcopy /E /I /Y /R "%~dp0machines\%~1\Language" "%~2\Language" >nul
if exist "%~dp0machines\%~1\PLCIni" xcopy /E /I /Y /R "%~dp0machines\%~1\PLCIni" "%~2\PLCIni" >nul
echo 已部署 %~1 語言檔到 %~2
