echo off

cls
echo Kopirivanie failov v directoriu

if not exist H:\bin (
mkdir H:\bin
for /R H:\ %%i in (*.*) do (
copy %%i H:\bin
)
)
echo on