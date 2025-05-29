eBay Product Listing Automation Guide
This guide outlines the step-by-step process to extract, clean, and prepare product data for eBay listing using a combination of Python scripts, Chrome extensions, and manual adjustments.

🔧 Workflow Steps:
1. Save Product Archive Pages
Save the product archive pages as .html files manually from your browser.

2. Extract Product URLs
Run Urlextractor.py to extract product URLs.
Output: Assets/ebay_product_urls.csv

3. Extract Product Data Using Chrome Extension
Use the PandasExtract Chrome extension to extract product data from the URLs.
Extract the following fields:
URL,Title,Price,Condition,Stitched,Occasion,Material,Brand,Pocket,Style,Season,Pattern,Sleeves,Color,Gender,Length,Work,Neck,Country of Origin

4. Prepare CSV Files
Paste extracted data (excluding Title Data) into Assets/Data.csv. (rename Col titles Manually)
Save the Title column separately as Assets/Title.csv.
Once done, Match Url with title, if they were correct or not.

5. Optimize Titles Using ChatGPT
Ask ChatGPT to optimize product titles using the following prompt:

Prompt:
Please read the attached CSV file. Focus only on the title column. For each row, modify the existing product title to make it:
- Optimized for eBay SEO
- More attractive to potential buyers
- No more than 80 characters
- Use OpenAI
- Save new column as New Tile.
- Rename the existing title column to Old Title.
- Capitalize the first letter of each word
- Return the modified CSV file with the same structure.

OR use Paste it on chatgpt in a group of 100.

Replace the old titles in Data.csv with optimized ones from the new Title.csv.

6. Download Product HTML Pages
Run Product-Html.py
Input: ebay_product_urls.csv
Output: HTML files saved to a corresponding folder. (if got any error at last, please ignore)

7. Extract Image URLs
Run Html2Img.py
Input: Product HTML files
Output: Assets/final_image_output.csv

8. Add Image URLs to Data
Copy the image URLs from final_image_output.csv to the corresponding rows in Data.csv.

9. Save Images and Create Data Files
Run Folder_Img_Data.py

This will:
Create folders for each product
Download images
Save a data.txt file in each product folder (based on Data.csv)

10. Clean Images
Run Clean_Img.py
This removes unwanted tags from images and saves them in a new cleanimg folder.

11. Generate Clean Data Text
Run Clean_Data.py
This creates dataclean.txt in each folder using data from Data.csv.

12. Remove Size Chart Images
Run Del_SizeChart.py
This script deletes size chart images from all image folders.

13. Extract Titles from Clean Data
Run title.py to extract product titles from dataclean.txt.

14. Extract Descriptions
Run description.py to generate product descriptions from dataclean.txt.

15. Upload to GitHub
Upload the entire folder structure (with cleaned data and images) to GitHub.

16. Generate Image Links
Run Img_Link.py to extract GitHub image URLs.
Output: imglink.txt

17. Format Image Links
Run Img_Link_Final.py to replace , with | in imglink.txt
Output: imglinkfinal.txt

18. Generate Final eBay Listing CSV
Run Final_CSV.py
Output: Assets/final_ebay_list.csv formatted as per eBay listing template.

Guide : https://pages.ebay.com/sh/reports/help/create-listings-bulk/#_nq6onyvjkyg
