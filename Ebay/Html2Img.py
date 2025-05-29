import os
import re
import csv
from bs4 import BeautifulSoup
from collections import defaultdict

# Base path to the saved HTML files
base_folder = "Ebaydata"
output_csv = "Assets/final_image_output.csv"
banned_code = "GH4AAOSwwt5lq2oh"

def extract_images_from_html(html_path):
    with open(html_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")

    image_map = defaultdict(lambda: ("", 0))  # code -> (url, resolution)

    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if src and "i.ebayimg.com" in src:
            match = re.search(r'/images/g/([^/]+)/s-l(\d+)', src)
            if match:
                code, res = match.groups()
                res = int(res)

                if code == banned_code or res <= 1000:
                    continue  # Skip banned code or low resolution

                # Keep highest resolution per code
                if res > image_map[code][1]:
                    image_map[code] = (src, res)

    return [img_url for img_url, _ in image_map.values()]

# Process all folders and extract cleaned image URLs
output_data = []
for i in range(1, 562):  # Folders from 1 to 561
    folder_path = os.path.join(base_folder, str(i))
    html_file = os.path.join(folder_path, "html.html")

    if os.path.exists(html_file):
        print(f"🔍 Processing folder {i}")
        image_urls = extract_images_from_html(html_file)
        output_data.append([i] + image_urls)

# Write final output CSV
with open(output_csv, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output_data)

print(f"\n✅ All image URLs (res > 1000) extracted and saved to {output_csv}")
