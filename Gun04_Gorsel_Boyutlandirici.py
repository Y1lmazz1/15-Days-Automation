import os
from PIL import Image

target_dir = os.path.expanduser("~/Desktop/Deneme_Alani")
output_dir = os.path.join(target_dir, "Optimize_Edilmis")

def resize_images():
    if not os.path.exists(target_dir):
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(target_dir):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(target_dir, filename)
            img = Image.open(img_path)
            
          
            w_percent = (800 / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            resized_img = img.resize((800, h_size), Image.Resampling.LANCZOS)
            resized_img.save(os.path.join(output_dir, filename), optimize=True, quality=85)

if __name__ == "__main__":
    resize_images()