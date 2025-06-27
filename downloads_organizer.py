import os
import shutil
from pathlib import Path

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

def move_files():
    for filename in os.listdir(downloads_folder):
        source_path = downloads_folder / filename

        if source_path.is_file():
            ext = source_path.suffix.lower()
            moved = False
            for folder, extensions in target_folders.items():
                if ext in extensions:
                    dest_folder = folder
                    if not dest_folder.exists():
                        print(f"{dest_folder} Does not exist")
                        break
                    shutil.move(str(source_path), str(dest_folder / filename))
                    moved = True
                    break
            if not moved:
                print(f"Ukjent filtype: {filename}")

if __name__ == "__main__":
    move_files()
