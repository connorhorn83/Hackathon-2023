import cv2 as cv
from pyzbar.pyzbar import decode
import urllib.request
import json
#import pprint
import re


def remove_characters(input_string, characters_to_remove):
    for char in characters_to_remove:
        input_string = input_string.replace(char, '')
    return input_string

def split_text_with_nested_parentheses(input_string):
    # Replace '(' with ' (' and ')' with ') ' to separate parentheses from other text
    modified_string = input_string.replace('(', ' (').replace(')', ') ')

    # Split the modified string using '(' as a delimiter
    parts = modified_string.split('(')

    # Create a list to hold the final result
    result = []

    # Process each part and append it to the result list
    for part in parts:
        if ')' in part:
            # If the part contains ')', split it using ')' as a delimiter
            subparts = part.split(')')
            result.append(subparts[0].strip() + ')')  # Append the first part with ')'
            result.extend(subparts[1:])  # Append the remaining subparts
        else:
            # Split the part on '\n' and add each part separately
            subparts = part.split('\n')
            result.extend(subparts)

    return result

def remove_contains_and_text_after(input_string):
    # Convert the list of strings back to a single string
    input_string = '\n'.join(input_string)
    
    # Find the index of the first occurrence of 'Contains'
    contains_index = input_string.find('Contains')
    
    # If 'Contains' is found, remove everything from that point to the end of the string
    if contains_index != -1:
        result = input_string[:contains_index]
    else:
        result = input_string  # 'Contains' not found, return the original string
    
    return result

def delete_char_at_index(input_string, index):
    if index < 0 or index >= len(input_string):
        return input_string  # Index is out of range, return the original string

    # Create a new string by concatenating the parts before and after the character to delete
    new_string = input_string[:index] + input_string[index + 1:]

    return new_string

def remove_word(string, word_to_remove):
    # Use str.replace() to remove the specified word
    result = string.replace(word_to_remove, '')
    return result

def delete_text_between_square_brackets(input_string):
    # Use regular expressions to delete text between '[' and ']'
    result = re.sub(r'\[.*?\]', '', input_string)
    return result

def run_function(image_url):

    # files = ['Celsius_Lemon_Lime.jpg', 'Sea_Salt_Chips.jpg', 'Smokehouse_BBQ.jpg', 'image_67204609.JPG', 'Hot_Fries.jpg']
    # out = files[2]

    # file_path = f'src\\data\\Test Images\\{out}'
    file_path = image_url



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
    # cv.imshow('img', resized_image)
    # cv.waitKey(0)

    # Decode the barcode
    barcodes = decode(resized_image)

    # Iterate through the detected barcodes and print their data
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f"Barcode Type: {barcode_type}, Data: {barcode_data}")

    if (barcode_type == 'EAN13') and len(barcodes) == 1:
        # Send barcode data
        barcode = barcode_data

        api_key = "3uolgunto7alfggycr830aerkvyu6k"
        url = f"https://api.barcodelookup.com/v3/products?barcode={barcode}&formatted=y&key={api_key}"

        # Sends API Call to site
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())

        barcode_number = data["products"][0]["barcode_number"]
        print("Barcode Number:", barcode_number)

        title = data["products"][0]["title"]
        print("Title:", title)


        # Extract the ingredients from the JSON data
        ingredients = data['products'][0]['ingredients']

        nutrition_facts = data['products'][0]['nutrition_facts']

        ingredients = remove_word(remove_word(ingredients, 'And/or'), 'And')
        ingredients = delete_text_between_square_brackets(ingredients)
        ingredients = split_text_with_nested_parentheses(ingredients)
        ingredients = remove_contains_and_text_after(ingredients)

        # Split ingredients into an array
        ingredient_list = ingredients.split(', ')

        # Add spaces before and after each ingredient, replacing '\n' with a space
        ingredient_list_with_spaces = [' ' + ingredient.strip().replace('\n', ' ') + ' ' for ingredient in ingredient_list]

        # Split the list elements based on double spaces
        final_ingredients = []
        for ingredient in ingredient_list_with_spaces:
            parts = ingredient.split('  ')  # Split on double spaces
            final_ingredients.extend(parts)

        # Filter out empty strings
        final_ingredients = [ingredient for ingredient in final_ingredients if ingredient.strip()]

        # Print the array of ingredients with double space separation
        print("Ingredients:")


        for i in range(len(final_ingredients)):
            final_ingredients[i] = remove_characters(final_ingredients[i], '/*()[].,:?')



        # Final Ingredients has all of the sorted data
        return final_ingredients, nutrition_facts
    
