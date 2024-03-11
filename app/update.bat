@echo off
cd /d %~dp0
call pyuic5 -x .\Window.ui -o ui.py
echo Recreated the ui.py