import os
import shutil

target_dir = os.path.expanduser("~/Desktop/Deneme_Alani")

extensions = {
    ".pdf": "Belgeler",
    ".docx": "Belgeler",
    ".txt": "Belgeler",
    ".jpg": "Resimler",
    ".png": "Resimler",
    ".zip": "Arsivler",
    ".mp4": "Videolar"
}

def organize():
    if not os.path.exists(target_dir):
        print("Hedef klasör bulunamadı.")
        return

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        
        if os.path.isfile(filepath):
            ext = os.path.splitext(filename)[1].lower()
            
            if ext in extensions:
                dest_folder = os.path.join(target_dir, extensions[ext])
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"Tasindi: {filename} -> {extensions[ext]}")

if __name__ == "__main__":
    organize()