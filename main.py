import requests
import cv2
import pytesseract as tess

#tess.pytesseract.tesseract_cmd = r'C:\Users\ahmad\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
#opsi jika menggunakan library manual
namagambar = "Enter name your picture book : "
img = cv2.imread(input(namagambar))
print("")

custom_config = r'--oem 3 --psm 6'
hasil = tess.image_to_string(img, config=custom_config)
print(hasil)
print("")

API_KEY = "API KEY GOOGLE SEARCH ENGINE"
SEARCH_ENGINE_ID = "ID GOOGLE SEARCH ENGINE"

page = 1
start = (page - 1) * 4 + 1

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={hasil}&start={start}"

data = requests.get(url).json()

search_items = data.get("items")

for i, search_item in enumerate(search_items, start=1):

    title = search_item.get("title")

    snippet = search_item.get("snippet")

    html_snippet = search_item.get("htmlSnippet")

    link = search_item.get("link")

    print("=" * 10, f"Result #{i+start-1}", "=" * 10)
    print("")
    print("Title:", title)
    print("")
    print("Description:", snippet)
    print("")
    print("URL:", link, "\n")
