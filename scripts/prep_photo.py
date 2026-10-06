import sys
import io
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path: str, output_path: str = "source-prepped.png"):
    # 1. إزالة الخلفية
    with open(input_path, "rb") as f:
        img_bytes = f.read()
    no_bg_bytes = remove(img_bytes)
    
    img_pil = Image.open(io.BytesIO(no_bg_bytes)).convert("RGBA")
    
    # 2. وضع خلفية بيضاء لضبط التباين
    white_bg = Image.new("RGBA", img_pil.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, img_pil).convert("L")
    
    # 3. تحسين الملامح والظلال
    img_np = np.array(composite)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(img_np)
    
    # 4. حفظ الصورة المجهزة
    cv2.imwrite(output_path, enhanced)
    print(f"✅ تم معالجة الصورة وحفظها باسم: {output_path}")

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prep_photo(src)