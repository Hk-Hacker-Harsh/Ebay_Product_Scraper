import os
from PIL import Image

# Base folder
parent_folder = "Ebaydata"

# Loop through product folders: 1, 2, ...
for folder in os.listdir(parent_folder):
    product_path = os.path.join(parent_folder, folder)
    img_folder = os.path.join(product_path, "img")
    clean_folder = os.path.join(product_path, "cleanimg")

    if os.path.isdir(img_folder):
        os.makedirs(clean_folder, exist_ok=True)

        for img_name in os.listdir(img_folder):
            img_path = os.path.join(img_folder, img_name)
            clean_path = os.path.join(clean_folder, img_name)

            try:
                with Image.open(img_path) as img:
                    # Optional: convert to RGB (some images may be in palette mode)
                    img = img.convert("RGB")

                    # Optional: slight crop to change perceptual hash
                    img = img.crop((0, 0, img.width - 2, img.height - 2))

                    # Save clean image (no metadata) with quality setting
                    img.save(clean_path, quality=95)

                    print(f"✅ Cleaned and saved: {clean_path}")
            except Exception as e:
                print(f"❌ Error processing {img_path}: {e}")

print("✅ All images cleaned and saved to 'cleanimg' folders.")
