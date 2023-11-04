# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:48:05 2023

@author: conno
"""

import pandas as pd
import re

def clean_text(text):
    # Remove special characters and keep only letters, numbers, spaces, and basic punctuation
    cleaned_text = re.sub(r'[^\w\s.,!?]', '', text)
    cleaned_text = cleaned_text.replace('<br />', '')  # Remove <br />
    cleaned_text = cleaned_text.replace(',br ', ', ')  # Remove <br />
    return cleaned_text

def search_components(components_list):
    file_path = r'C:\Users\conno\OneDrive\Desktop\Hackathon\FoodSubstances.xlsx'  # Replace with the path to your Excel file
    sheet_name = 'FoodSubstances'  # Replace with the name of your sheet if different
    columns_of_interest = ['Name', 'Use']

    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        selected_data = data[columns_of_interest]
        
        indexed_data = selected_data.set_index('Name', drop=False)
        indexed_data.index = indexed_data.index.str.lower()

        for component in components_list:
            print(f"Searching for '{component}':")
            search_item = component.lower()
            found_items = indexed_data[indexed_data.index.str.contains(search_item, case=False, na=False)]

            if not found_items.empty:
                print("Results:")
                for index, row in found_items.iterrows():
                    cleaned_name = clean_text(index)  # Clean the 'Name' column text
                    cleaned_use = clean_text(row['Use'])  # Clean the 'Use' column text
                    print(f"Name: {cleaned_name}, Use: {cleaned_use}")
            else:
                print("No items found matching the search criteria for", component)
            print("\n")

    except FileNotFoundError:
        print("File not found. Please provide the correct file path.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage: Call the function and pass a list of components from another method (temp)
temp = ['Biotin', ' ascorbic acid', 'pantothenic']
search_components(temp)