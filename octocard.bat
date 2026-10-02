@echo off
chcp 65001 > nul

REM octocard.bat - one-click launch of "no-reminder-agent"
REM Workspace at C:\Users\steam\Desktop\octo\octosense-ws

setlocal
set "WORKSPACE=%~dp0octosense-ws"
set "CARD_HOST=%~dp0OctoSense-App-Hub\target\release\card-host.exe"
set "APP=%WORKSPACE%\apps\no-reminder-agent\bundle"

REM Kill any old card-host
taskkill /F /IM card-host.exe > nul 2>&1

echo === octocard: launching "no-reminder-agent" ===
echo workspace: %WORKSPACE%
echo port:      8141
echo.

REM Set headless mode + start card-host in background (uses inherited cwd, but absolute paths work)
set MAKEPAD_HIDE_WINDOWS=1
start "octocard-app" /B "%CARD_HOST%" --bundle "%APP%" --allow-unsigned --stamp --remote 8141

echo === app starting in background (waiting 5s)... ===
ping -n 6 127.0.0.1 > nul

echo === ready! Try: ===
echo   curl -s 127.0.0.1:8141/snap          REM check UI
echo   curl -s 127.0.0.1:8141/quit          REM stop app
echo.

endlocal
