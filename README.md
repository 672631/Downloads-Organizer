# Downloads Organizer
A background script that automatically sorts downloaded files into the appropriate folders like Documents, Pictures, Videos, and Music right after the files are downloaded. 

## Features

- Moves files from 'Downloads' or 'Nedlastinger' to the target folders:
  - OneDrive/Dokumenter
  - OneDrive/Bilder
  - OneDrive/Videos
  - OneDrive/Musikk
- Real-time file watching using 'watchdog'
- Compiled to a .exe file
- Configured to launch on Windows startup by scheduling in 'Task Scheduler'

## Customizing Folder Paths

The script uses fixed folder names like `OneDrive/Dokumenter`, `OneDrive/Bilder`, etc.  
These paths may vary depending on your system language, OneDrive setup, or user preferences.

### Requirements
Install dependencies: 

```bash
pip install watchdog
```
## Compile to EXE
```bash
pip install pyinstaller #Install pyinstaller if you haven't already
pyinstaller --noconsole --onefile downloads_organizer.py
```
The resulting executable will be place in the dist/ folder in your repository

## Launch on Startup (Windows)

1. Open Task Scheduler
2. Create new basic task
3. Set the trigger to "At log on"
4. For the action, point to your .exe file
5. Enable "Run wheter user is logged in or not" and "Run with highest priveleges"


