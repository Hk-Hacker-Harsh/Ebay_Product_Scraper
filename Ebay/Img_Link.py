import os

# GitHub info
github_username = "Test197-root"
repo_name = "Ebaydata"
branch = "refs/heads/main"

# Local Ebaydata folder
local_base = "Ebaydata"

# Raw GitHub base URL
url_base = f"https://raw.githubusercontent.com/{github_username}/{repo_name}/{branch}"

# Process folders 1 to 561
for i in range(1, 562):
    folder = str(i)
    local_folder = os.path.join(local_base, folder)
    cleanimg_folder = os.path.join(local_folder, "cleanimg")
    imglink_path = os.path.join(local_folder, "imglink.txt")

    if not os.path.isdir(cleanimg_folder):
        print(f"⚠️ Missing cleanimg folder in: {folder}")
        continue

    links = []
    for filename in sorted(os.listdir(cleanimg_folder)):
        if filename.lower().endswith(".webp"):
            url = f"{url_base}/{folder}/cleanimg/{filename}"
            links.append(url)

    if links:
        with open(imglink_path, "w", encoding="utf-8") as f:
            f.write(",".join(links))
        print(f"✅ Created imglink.txt in folder {folder}")
    else:
        print(f"⚠️ No .webp images in: {cleanimg_folder}")

print("🎉 All imglink.txt files generated.")
