@echo off
chcp 65001 > nul

REM octocard.bat - one-click launch of "no-reminder-agent"
REM Workspace at C:\Users\steam\Desktop\octo\octosense-ws

setlocal
if not defined OCTO_CARD_HOST set "OCTO_CARD_HOST=%~dp0..\octosense-ws\OctoSense-App-Hub\target\release\card-host.exe"
if not exist "%OCTO_CARD_HOST%" (
  echo Set OCTO_CARD_HOST to the full path of card-host.exe. See README.zh-CN.md.
  exit /b 2
)
set "MAKEPAD_HIDE_WINDOWS="
"%OCTO_CARD_HOST%" --bundle "%~dp0bundle" --app-data "%~dp0.local-state" --allow-unsigned
set "octo_launch_exit=%ERRORLEVEL%"
endlocal & exit /b %octo_launch_exit%

