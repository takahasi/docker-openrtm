@echo off

set INSTALLER=InstallDocker.exe

rem for Windows 10 Pro (Latest)
set URL="https://download.docker.com/win/stable/Docker for Windows Installer.exe"

rem for Windows 7/8/8.1 (Legacy)
rem set URL="https://download.docker.com/win/stable/DockerToolbox.exe"

cd /d %~dp0
bitsadmin /RawReturn /TRANSFER download %URL% %CD%\%INSTALLER%

call %INSTALLER%
del /q %INSTALLER%

pause
exit