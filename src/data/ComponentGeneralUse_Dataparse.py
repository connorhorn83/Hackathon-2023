# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 13:48:05 2023

@author: conno
"""

import pandas as pd
import re
from BarcodeAPIDataSplit import run_function
from HealthEffects import found_in_db
import wikipedia

def search_term(component):
    return wikipedia.summary(component, sentences=4, auto_suggest=False) + "\n"

def clean_text(text):
    # Ensure 'text' is a string before cleaning
    if isinstance(text, str):
        # Remove special characters and keep only letters, numbers, spaces, and basic punctuation
        cleaned_text = re.sub(r'[^\w\s.,!?]', '', text)
        cleaned_text = cleaned_text.replace('<br />', '')  # Remove <br />
        cleaned_text = cleaned_text.replace(',br ', ', ')  # Remove <br /
        return cleaned_text
    else:
        return str(text)  # Convert non-string data to string and return

def search_components(components_list):
    for i in range(len(components_list)):
        if ' ' in components_list:
            components_list.remove(' ')
    file_path = r"src/data/FoodSubstances.xlsx"
    sheet_name = 'FoodSubstances'
    columns_of_interest = ['Name', 'Use',]
    df_list = []  # Empty list to store individual DataFrames

    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        selected_data = data[columns_of_interest]
        
        indexed_data = selected_data.set_index('orig_components_name', drop=False)
        indexed_data.index = indexed_data.index.str.lower()
        
        for component in components_list:
            #print(component)
            print(f"Searching for '{component}':")
            search_item = r"\b" + re.escape(component.lower()) + r"\b"  # Use regex word boundaries
            found_items = indexed_data[indexed_data.index.str.contains(search_item, case=False, na=False, regex=True)]

            if not found_items.empty:
                df_list.append(found_items)  # Append found DataFrame slices to the list
                print("Results:")
                for index, row in found_items.iterrows():
                    cleaned_name = clean_text(str(index))  # Clean the 'Name' column text
                    cleaned_use = clean_text(str(row['Use']))  # Clean the 'Use' column text
                    print(f"Name: {cleaned_name}, Use: {cleaned_use}")
            else:
                print("No items found matching the search criteria for", component)
            print("\n")

        df_combined = pd.concat(df_list, ignore_index=True) if df_list else pd.DataFrame()  # Combine individual DataFrames into a single DataFrame

        df_combined['Use'] = df_combined['Use'].apply(clean_text)
        # summary_list = []
        for i in range(len(df_combined['Use'])):
            # summary_list.append((search_term(df_combined['Name'][i])))
            if df_combined['Use'][i] == 'nan':
                df_combined['Use'][i] = 'THE FDA PROVIDES NO INFORMATION ON THIS COMPONENT'
        # df_combined['Summary'] = summary_list
        return df_combined
            

    except FileNotFoundError:
        print("File not found. Please provide the correct file path.")
    except Exception as e:
        print("An error occurred:", e)

    # Example usage: Call the function and pass a list of components from another method (temp)
def ingredient_list_search():
    final_ingredients, nutrition_facts = run_function()
    temp = final_ingredients
    search_components(temp)
    print(final_ingredients)

def run_processing(image_url):
    final_ingredients, nutrition_facts = run_function(image_url)
    df = search_components(final_ingredients)
    df = found_in_db(df)
    return df
    
temp = ['caffeine']
df = search_components(temp)
df = found_in_db(df)
print(df.head())