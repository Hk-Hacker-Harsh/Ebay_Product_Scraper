from bs4 import BeautifulSoup
import pandas as pd

# List of input HTML files
html_files = ["Assets/Page1.html", "Assets/Page2.html", "Assets/Page3.html"]

# Collect all product URLs
all_urls = []

for file_name in html_files:
    with open(file_name, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        for a in soup.find_all("a", href=True):
            href = a['href']
            if "/itm/" in href:
                all_urls.append(href)

# Remove duplicates (optional)
all_urls = list(set(all_urls))

# Save to CSV
df = pd.DataFrame(all_urls, columns=["URL"])
df.to_csv("Assets/ebay_product_urls.csv", index=False)

print("✅ Extracted URLs saved to 'Assets/ebay_product_urls.csv'")
