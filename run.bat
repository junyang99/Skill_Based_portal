@echo off

REM Set the root directory of your Git repository
set ROOT_DIR=%CD%

REM Run HR Flask apps
for %%i in ("%ROOT_DIR%\HR\*.py") do (
  start cmd /k "python %%i"
)

REM Run utils Flask apps
for %%i in ("%ROOT_DIR%\utils\*.py") do (
  start cmd /k "python %%i"
)

REM Install dependencies and run the UI
cd skill-based-portal
start cmd /k "npm install && npm run serve"
