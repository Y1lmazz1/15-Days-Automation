import os

target_dir = os.path.expanduser("~/Desktop/Deneme_Alani")

def bulk_rename():
    if not os.path.exists(target_dir):
        return

    files = os.listdir(target_dir)
    count = 1

    for filename in files:
        old_path = os.path.join(target_dir, filename)
        
        if os.path.isfile(old_path):
            extension = os.path.splitext(filename)[1]
            new_name = f"Belge_{count}{extension}"
            new_path = os.path.join(target_dir, new_name)
            
            os.rename(old_path, new_path)
            count += 1

if __name__ == "__main__":
    bulk_rename()