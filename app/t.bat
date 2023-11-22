@echo off
cd /d %~dp0
call pyuic5 -x .\Window.ui -o hello.py
echo Recreated the hello.py