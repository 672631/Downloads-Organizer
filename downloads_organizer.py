import shutil
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Folder setup
home = Path.home()
downloads_folder = home / "Downloads"
if not downloads_folder.exists():
    downloads_folder = home / "Nedlastinger"

target_folders = {
    home / "OneDrive/Dokumenter": [".pdf", ".docx", ".txt", ".pptx"],
    home / "OneDrive/Bilder": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    home / "OneDrive/Videos":[".mp4", ".mov", ".avi"],
    home / "OneDrive/Musikk":[".mp3", ".wav"]
}

#Function for moving files to appropriate directory
def move_files(path: Path):
    
    ext = path.suffix.lower()

    for dest_folder, extensions in target_folders.items():
        if ext in extensions:
            if not dest_folder.exists():
                print(f"{dest_folder} does not exist")
                return
            try:
                shutil.move(str(path), str(dest_folder / path.name))
                print(f"Moved {path.name} -> {dest_folder}")
            except Exception as e: 
                print(f"Could not move {path.name}: {e}")
            return

#Watchdog event handler
class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            time.sleep(3)
            move_files(Path(event.src_path))

    def on_modified(self, event):
        if not event.is_directory:
            time.sleep(3)
            move_files(Path(event.src_path))

#Watching function
def watching():
    observer = Observer()
    observer.schedule(DownloadHandler(), str(downloads_folder), recursive = False)
    observer.start()
    print(f"Watching for downloads in: {downloads_folder}")
    try: 
        while True: 
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    watching()
