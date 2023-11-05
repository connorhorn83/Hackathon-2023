# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 00:51:27 2023

@author: conno
"""

import pandas as pd

#df = pd.DataFrame("Comp.", [1],"q/1000",[1],"Score",[1])

# add code to take in nutrition facts from barcode in list format
# ['Component_1 Quantity_1 Unit_1','Component_2 Quantity_2 Unit_2'] 

input_string = ('Energy 540 kcal, Fat 30.85 g, Saturated Fat 5.14 g, '
                'Carbohydrates 59.13 g, Sugars 7.71 g, Fiber 5.1 g, '
                'Protein 5.14 g, Salt 1.285 g, Vitamin A 0.0003084 g, '
                'Vitamin C 0.0231 g, Potassium 1.234 g, Iron 0.00185 g.')

def data_organize(input_string):
    # Splitting the string into components
    components = input_string.split(', ')

    # Creating a list to store the parsed components
    parsed_components = []

    for item in components:
        value_start = next((i for i, c in enumerate(item) if c.isdigit()), None)
        if value_start:
            name = item[:value_start - 1].replace('.', '')  # Extract the name before the numeric value and remove periods
            quantity_unit = item[value_start:].split()  # Split the quantity and unit
            quantity = quantity_unit[0] if len(quantity_unit) > 0 else None
            unit = quantity_unit[1].replace('.', '') if len(quantity_unit) > 1 else None  # Remove periods from the unit
        else:
            name = item.replace('.', '')  # Remove periods from the name
            quantity = None
            unit = None

        parsed_components.append({'Name': name, 'Quantity': quantity, 'Unit': unit})

    return parsed_components


def calculate_dv_score(nutrient_name, quantity, unit):
    # Dictionary containing the maximum recommended values for various nutrients
    dv_max_values = {
        'Fat': 61,  # Replace with the actual maximum value for fat
        'Vitamin A': 0.8,  # Replace with the actual maximum value for Vitamin A
        'Carbohydrates': 275,
        'Saturated Fat': 22,
        'Salt': 5.9,
        'Sodium': 2.3,
        'Potassium': 2.88,
        'Fiber': 27.5,
        'Iron': 0.012,
        'Protein': 50,
        'Vitamin B': 0.0028,
        'Vitamin D': 0.015,
        'Vitamin C': 0.08,
        'Vitamin E': 0.015,
        'Sugars': 30,
        'Energy': 2000,
        
        
    }
    # Convert ounces to grams
    if unit.lower() == 'oz':
        try:
            quantity = float(quantity)
            quantity *= 28.35  # 1 oz = 28.35 grams
            unit = 'g'
        except ValueError:
            return "Quantity should be a number"

    if nutrient_name in dv_max_values:
        max_value = dv_max_values[nutrient_name]

        try:
            quantity = float(quantity)
            dv_score = (quantity / max_value) * 10
            return str(round(dv_score,2)) + '/10'
        except ValueError:
            return "Quantity should be a number"
    else:
        return "Nutrient not found or not supported for DV score calculation"

nutrient_data = data_organize(input_string)

for nutrient in nutrient_data:
    nutrient_name = nutrient.get('Name')
    nutrient_quantity = nutrient.get('Quantity')
    nutrient_unit = nutrient.get('Unit')

    score = calculate_dv_score(nutrient_name, nutrient_quantity, nutrient_unit)
    print(nutrient_name, ": ",score)
