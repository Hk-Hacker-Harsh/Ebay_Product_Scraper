import pandas as pd
import os
import requests
from urllib.parse import urlparse

# Load the CSV with correct encoding
df = pd.read_csv("Assets/Data.csv", encoding="windows-1252")

# Define parent folder
parent_folder = "Ebaydata"
os.makedirs(parent_folder, exist_ok=True)

# Process each row in the CSV
for index, row in df.iterrows():
    # Create folder path: Ebaydata/1, Ebaydata/2, etc.
    product_folder = os.path.join(parent_folder, str(index + 1))
    img_folder = os.path.join(product_folder, "img")
    os.makedirs(img_folder, exist_ok=True)

    # Save non-image data to data.txt
    with open(os.path.join(product_folder, "data.txt"), "w", encoding="utf-8") as f:
        for col in df.columns:
            value = str(row[col]).strip()
            if not value.lower().startswith("http"):
                f.write(f"{col}: {value}\n")

    # Download images as 1.jpg, 2.jpg, ...
    img_count = 1
    for col in df.columns:
        url = str(row[col]).strip()
        if url.lower().startswith("http") and any(ext in url.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                ext = os.path.splitext(urlparse(url).path)[1]
                ext = ext if ext.lower() in ['.jpg', '.jpeg', '.png', '.webp'] else '.jpg'
                filename = f"{img_count}{ext}"
                filepath = os.path.join(img_folder, filename)

                with open(filepath, "wb") as img_file:
                    img_file.write(response.content)

                print(f"✅ Downloaded {filename} in {product_folder}")
                img_count += 1
            except Exception as e:
                print(f"❌ Failed to download from {url}: {e}")

print("✅ All products saved inside 'Ebaydata' folder.")
