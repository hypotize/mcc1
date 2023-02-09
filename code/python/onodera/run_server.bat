@echo off
 
for /f "tokens=1,2* usebackq delims=^:" %%i in (`ipconfig ^| findstr /n /r "." ^| findstr /r "IPv4 アドレス"`) DO @set IP=%%k

call :Trim %IP%

:Trim
set IP=%*

echo uvicorn main:app --reload --host %IP% --port 8000

uvicorn main:app --reload --host %IP% --port 8000