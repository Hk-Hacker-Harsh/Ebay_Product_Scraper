import os

BASE_PATH = "Ebaydata"

def recreate_title(original_title: str) -> str:
    # Basic enhancement – makes it more click-worthy
    return f"{original_title}"

# Loop through folders
for i in range(1, 562):
    folder_path = os.path.join(BASE_PATH, str(i))
    dataclean_path = os.path.join(folder_path, "dataclean.txt")
    title_txt_path = os.path.join(folder_path, "title.txt")

    if os.path.exists(dataclean_path):
        with open(dataclean_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Extract title
        original_title = ""
        for line in lines:
            if line.startswith("Title:"):
                original_title = line.split(":", 1)[1].strip()
                break

        if original_title:
            # Recreate title
            new_title = recreate_title(original_title)

            # Save to title.txt
            with open(title_txt_path, "w", encoding="utf-8") as out_file:
                out_file.write(new_title)

            print(f"[✅] Title updated: {title_txt_path}")
        else:
            print(f"[⚠️] Title missing in: {dataclean_path}")
    else:
        print(f"[🚫] Missing file: {dataclean_path}")
