import os

BASE_PATH = "Ebaydata"

def generate_description(data: str) -> str:
    lines = data.strip().split("\n")
    info = {}
    for line in lines:
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()

    # Grab necessary fields with fallbacks
    title = info.get("Title", "this ethnic outfit")
    material = info.get("Material", "high-quality fabric")
    color = info.get("Color", "a beautiful color blend")
    work = info.get("Work", "")
    pattern = info.get("Pattern", "")
    sleeves = info.get("Sleeves", "")
    neck = info.get("Neck", "")
    occasion = info.get("Occasion", "special occasions")
    season = info.get("Season", "all seasons")
    stitched = info.get("Stitched", "")
    origin = info.get("Country of Origin", "India")

    # Paragraph Description
    description = f"""Description:
Experience elegance and comfort with {title}, thoughtfully crafted for {occasion}. Designed in {material}, this fully {stitched.lower()} outfit features a stunning {pattern.lower()} enhanced with {work.lower()}. The eye-catching {color.lower()} tones add a stylish flair, while the {sleeves.lower()} and {neck.lower()} design offer a perfect blend of tradition and modern aesthetics. Ideal for {season.lower()}, this outfit is a must-have in every wardrobe. Proudly handmade in {origin}, it reflects timeless craftsmanship and grace.
"""

    # Append bullet-style details
    keys_to_show = [
        "Title", "Price", "Occasion", "Material", "Brand", "Style", "Season", "Pattern",
        "Sleeves", "Color", "Gender", "Length", "Work", "Neck", "Country of Origin"
    ]
    description += "\nDetails:\n"
    for key in keys_to_show:
        if key in info:
            description += f"- {key}: {info[key]}\n"


    return description

# Loop through folders 1 to 561
for i in range(1, 562):
    folder_path = os.path.join(BASE_PATH, str(i))
    dataclean_path = os.path.join(folder_path, "dataclean.txt")
    description_path = os.path.join(folder_path, "description.txt")

    if os.path.exists(dataclean_path):
        with open(dataclean_path, "r", encoding="utf-8") as file:
            raw_data = file.read()

        # Generate description
        description = generate_description(raw_data)

        # Save to description.txt
        with open(description_path, "w", encoding="utf-8") as out_file:
            out_file.write(description)

        print(f"[✅] Created: {description_path}")
    else:
        print(f"[⚠️] Missing: {dataclean_path}")
