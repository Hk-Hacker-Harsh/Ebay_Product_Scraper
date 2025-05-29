import os
import pandas as pd

# Load the cleaned CSV with headers
df = pd.read_csv("Assets/Data.csv", encoding="cp1252")  # Using Windows-friendly encoding

# Folder containing product folders
parent_folder = "Ebaydata"

# Loop through rows in the DataFrame
for index, row in df.iterrows():
    folder_index = index + 1  # Folder "1" corresponds to row 0 (excluding header)
    product_folder = os.path.join(parent_folder, str(folder_index))

    if os.path.isdir(product_folder):
        dataclean_path = os.path.join(product_folder, "dataclean.txt")

        # Write key-value pairs to dataclean.txt, excluding eBay image URLs
        with open(dataclean_path, "w", encoding="utf-8") as f:
            for col in df.columns:
                value = str(row[col]).strip()
                if (
                    value.lower() != "nan"
                    and value != ""
                    and "i.ebayimg.com" not in value.lower()
                ):
                    f.write(f"{col}: {value}\n")

        print(f"✅ Created: {dataclean_path}")
    else:
        print(f"⚠️ Folder not found: {product_folder}")

print("✅ All dataclean.txt files created.")
