import csv
import os
import re



# ========== CONFIGURABLE VARIABLES ==========
multi_color_count = 0

base_path = r"C:\Users\KPK\Desktop\Present\Ebay"
input_csv_path = os.path.join(base_path, "Assets/eBay-template.csv")
output_csv_path = os.path.join(base_path, "Assets/final_ebay_list.csv")
product_base_folder = os.path.join(base_path, "Ebaydata")
max_products = 561
variation_sizes = ["XS", "S", "M", "L", "XL", "XXL"]

# Proper column header
columns_line = """
*Action(SiteID=US|Country=US|Currency=USD|Version=1193|CC=UTF-8)	CustomLabel	*Category	StoreCategory	*Title	Subtitle	Relationship	RelationshipDetails	ScheduleTime	*ConditionID	C:Style	C:Gender	C:Size	C:Material	C:Brand	C:Country/Region of Manufacture	C:MPN	C:Color	C:California Prop 65 Warning	PicURL	GalleryType	VideoID	*Description	*Format	*Duration	*StartPrice	BuyItNowPrice	BestOfferEnabled	BestOfferAutoAcceptPrice	MinimumBestOfferPrice	*Quantity	ImmediatePayRequired	*Location	ShippingType	ShippingService-1:Option	ShippingService-1:Cost	ShippingService-2:Option	ShippingService-2:Cost	*DispatchTimeMax	PromotionalShippingDiscount	ShippingDiscountProfileID	*ReturnsAcceptedOption	ReturnsWithinOption	RefundOption	ShippingCostPaidByOption	AdditionalDetails	ShippingProfileName	ReturnProfileName	PaymentProfileName	ProductCompliancePolicyID	Regional ProductCompliancePolicies	Product Safety Pictograms	Product Safety Statements	Product Safety Component	Regulatory Document Ids	Manufacturer Name	Manufacturer AddressLine1	Manufacturer AddressLine2	Manufacturer City	Manufacturer Country	Manufacturer PostalCode	Manufacturer StateOrProvince	Manufacturer Phone	Manufacturer Email	Manufacturer ContactURL	Responsible Person 1	Responsible Person 1 Type	Responsible Person 1 AddressLine1	Responsible Person 1 AddressLine2	Responsible Person 1 City	Responsible Person 1 Country	Responsible Person 1 PostalCode	Responsible Person 1 StateOrProvince	Responsible Person 1 Phone	Responsible Person 1 Email	Responsible Person 1 ContactURL
""".strip()
column_names = columns_line.split('\t')

# Template for parent row fields
static_fields_parent = {
    "*Action(SiteID=US|Country=US|Currency=USD|Version=1193|CC=UTF-8)": "Add",
    "*Category": "155249",
    "*ConditionID": "1500",
    "C:Style": "Salwar Kameez",
    "C:Gender": "Women",
    "C:Country/Region of Manufacture": "India",
    "*Format": "FixedPrice",
    "*Duration": "10",
    "*Location": "India",
    "RelationshipDetails": "Size=XS;S;M;L;XL;XXL",
    "ShippingService-1:Option":"USPSStandardPost",
    "ShippingService-1:Cost":"0.00",
    "*ReturnsAcceptedOption":"ReturnsAccepted",
    "*DispatchTimeMax":"7"
}

# Helper to make blank row
def create_blank_row():
    return [''] * len(column_names)

# Start output list
output_rows = [column_names]

# Loop through product folders
for i in range(1, max_products + 1):
    folder_path = os.path.join(product_base_folder, str(i))

    # Required file paths
    title_path = os.path.join(folder_path, "title.txt")
    description_path = os.path.join(folder_path, "description.txt")
    img_link_path = os.path.join(folder_path, "imglinkfinal.txt")
    dataclean_path = os.path.join(folder_path, "dataclean.txt")

    for path in [title_path, description_path, img_link_path, dataclean_path]:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Missing file: {path} for product {i}")

    # Read data
    with open(title_path, 'r', encoding='utf-8') as f:
        title = f.read().strip()
    with open(description_path, 'r', encoding='utf-8') as f:
        description = f.read().strip()
    with open(img_link_path, 'r', encoding='utf-8') as f:
        img_links = f.read().strip()

    # Extract price and material from dataclean.txt
    with open(dataclean_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        price_line = next((line for line in lines if line.startswith("Price:")), None)
        if not price_line:
            raise ValueError(f"No price found in {dataclean_path}")
        price_match = re.search(r"US\s*\$(\d+(\.\d{1,2})?)", price_line)
        if not price_match:
            raise ValueError(f"Invalid price format in: {price_line}")
        price = price_match.group(1)

        material_line = next((line for line in lines if line.startswith("Material:")), None)
        if not material_line:
            raise ValueError(f"Material not found in {dataclean_path}")
        material = material_line.split("Material:")[1].strip()

        color_line = next((line for line in lines if line.startswith("Color:")), None)
        if not color_line:
            raise ValueError(f"Color not found in {dataclean_path}")
        color = color_line.split("Color:")[1].strip()

        brand_line = next((line for line in lines if line.startswith("Brand:")), None)
        if not brand_line:
            raise ValueError(f"Brand not found in {dataclean_path}")
        brand = brand_line.split("Brand:")[1].strip()

        # Show color options if multiple
        normalized_color = color.lower()
        multi_match = any(keyword in normalized_color for keyword in ["multi", " or ", "-", "/", "&", ",", " and "])
        color_list = [c.strip().title() for c in re.split(r"\s*(?:&|,|And|AND|and|or|/|-)\s*", color) if c.strip()]

        if multi_match or len(color_list) > 1:
            multi_color_count += 1
            print(f"\nProduct {i} has multiple colors:")
            for idx, col in enumerate(color_list, start=1):
                print(f"  {idx}. {col}")
    


    # Build Parent Row
    parent_row = create_blank_row()
    for key, value in static_fields_parent.items():
        if key in column_names:
            parent_row[column_names.index(key)] = value
    if "*Title" in column_names:
        parent_row[column_names.index("*Title")] = title
    if "PicURL" in column_names:
        parent_row[column_names.index("PicURL")] = img_links
    if "*Description" in column_names:
        parent_row[column_names.index("*Description")] = description
    if "C:Material" in column_names:
        parent_row[column_names.index("C:Material")] = material
    output_rows.append(parent_row)
    if "C:Color" in column_names:
        parent_row[column_names.index("C:Color")] = color
    if "C:Brand" in column_names:
        parent_row[column_names.index("C:Brand")] = brand

    # Build Child Rows
    for size in variation_sizes:
        child_row = create_blank_row()
        if "Relationship" in column_names:
            child_row[column_names.index("Relationship")] = "Variation"
        if "RelationshipDetails" in column_names:
            child_row[column_names.index("RelationshipDetails")] = f"Size={size}"
        if "*StartPrice" in column_names:
            child_row[column_names.index("*StartPrice")] = price
        if "*Quantity" in column_names:
            child_row[column_names.index("*Quantity")] = "1"
        output_rows.append(child_row)

# Save output CSV
with open(output_csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(output_rows)

print(f"\n Total products with multiple colors: {multi_color_count}")
print(f" Done! Output saved to: {output_csv_path}")