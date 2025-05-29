import os
import csv
import time
import undetected_chromedriver as uc

csv_file = "Assets/ebay_product_urls.csv"
base_folder = "Ebaydata"

# Load URLs
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    urls = [row[0].strip() for row in reader if row]

# Start stealth browser
options = uc.ChromeOptions()
options.add_argument("--headless")  # Optional: run without opening window
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = uc.Chrome(options=options)

for i, url in enumerate(urls[:561], start=1):
    folder_path = os.path.join(base_folder, str(i))
    os.makedirs(folder_path, exist_ok=True)
    html_path = os.path.join(folder_path, "html.html")

    try:
        print(f"🌐 [{i}] Visiting: {url}")
        driver.get(url)
        time.sleep(5)  # Wait for JS to load
        html = driver.page_source

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Saved: {html_path} ({len(html.encode('utf-8'))} bytes)")

    except Exception as e:
        print(f"❌ Error on [{i}] {url}: {e}")

driver.quit()
