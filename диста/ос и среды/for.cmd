@echo off
if not exist bin mkdir bin
for /r %%i in (*.*) do echo %%i
echo on