import cv2 as cv
from pyzbar.pyzbar import decode
import urllib.request
import json
import pprint

api_key = "3uolgunto7alfggycr830aerkvyu6k"
barcode = "072180634733"
url = f"https://api.barcodelookup.com/v3/products?barcode={barcode}&formatted=y&key={api_key}"



files = ['Celsius_Lemon_Lime.jpg', 'Sea_Salt_Chips.jpg', 'Smokehouse_BBQ.jpg', 'image_67204609.JPG', 'Hot_Fries.jpg']
out = files[2]

file_path = rf'MakeUC 2023\Test Images\{out}'

input_image = cv.imread(file_path)

# Used to scale the input image properly
max_dimension = 800  # You can change this value as needed
height, width, _ = input_image.shape

if width > height:
    new_width = max_dimension
    new_height = int(height * (max_dimension / width))
else:
    new_height = max_dimension
    new_width = int(width * (max_dimension / height))

# Resize the image
resized_image = cv.resize(input_image, (new_width, new_height))

# Show the resized image
cv.imshow('img', resized_image)
cv.waitKey(0)

# Decode the barcode
barcodes = decode(resized_image)

# Iterate through the detected barcodes and print their data
for barcode in barcodes:
    barcode_data = barcode.data.decode('utf-8')
    barcode_type = barcode.type
    print(f"Barcode Type: {barcode_type}, Data: {barcode_data}")

if (barcode_type == 'EAN13') and len(barcodes) == 1:
    # Sends API Call to site
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    barcode_number = data["products"][0]["barcode_number"]
    print("Barcode Number:", barcode_number)

    title = data["products"][0]["title"]
    print("Title:", title)

    print("Entire Response:")
    pprint.pprint(data)

    # Save the data to a JSON file
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)

