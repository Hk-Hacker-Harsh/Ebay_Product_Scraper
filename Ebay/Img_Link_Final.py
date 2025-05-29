import os

base_dir = "Ebaydata"
output_filename = "imglinkfinal.txt"

for folder_number in range(1, 562):  # 1 to 561 inclusive
    folder_path = os.path.join(base_dir, str(folder_number))
    input_file = os.path.join(folder_path, "imglink.txt")
    output_file = os.path.join(folder_path, output_filename)

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            data = f.read()
        modified_data = data.replace(",", "|")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(modified_data)

        print(f"[+] Converted: {input_file} → {output_file}")

    except FileNotFoundError:
        print(f"[!] Skipped: {input_file} (file not found)")
    except Exception as e:
        print(f"[!] Error processing {input_file}: {e}")
