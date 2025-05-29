import os
import cv2
from skimage.metrics import structural_similarity as ssim

# Config
target_img_path = "Assets/reference-size-chart.webp"  # change this to your image path
base_folder = "Ebaydata"
SIMILARITY_THRESHOLD = 0.50
total_folders = 561

# Load and preprocess target image
def load_gray_resized(path, size=(300, 300)):
    img = cv2.imread(path)
    if img is None:
        raise Exception(f"Cannot read image: {path}")
    img = cv2.resize(img, size)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

target_img = load_gray_resized(target_img_path)

# Loop through each folder
deleted = 0
for i in range(1, total_folders + 1):
    print(f"📁 Processing folder {i}/{total_folders}...")
    folder_path = os.path.join(base_folder, str(i), "cleanimg")

    if not os.path.isdir(folder_path):
        print("🚫 Folder not found, skipping...")
        continue

    for file in os.listdir(folder_path):
        img_path = os.path.join(folder_path, file)
        if not os.path.isfile(img_path):
            continue

        try:
            img = load_gray_resized(img_path)
            score, _ = ssim(target_img, img, full=True)

            if score >= SIMILARITY_THRESHOLD:
                os.remove(img_path)
                print(f"🗑️ Deleted: {img_path} (SSIM: {score:.3f})")
                deleted += 1

        except Exception as e:
            print(f"❌ Error with {img_path}: {e}")

print(f"\n✅ Completed all folders. Total deleted: {deleted}")
