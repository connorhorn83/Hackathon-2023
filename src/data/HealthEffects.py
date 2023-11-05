# import pandas as pd

# def get_health_effects_file():
#     file_path = r"src/data/CompoundsHealthEffect.xlsx"
#     sheet_name = 'CompoundsHealthEffect'
#     data = pd.read_excel(file_path, sheet_name=sheet_name)
#     columns_of_interest = ['orig_compound_name', 'orig_health_effect_name']
#     data = data[columns_of_interest]
#     result = data.groupby('orig_compound_name')['orig_health_effect_name'].agg(concatenate_health_effects).reset_index()
#     print(result)
#     return result
    
# def concatenate_health_effects(series):
#     return ', '.join(series)

# def found_in_db(final_ingredients):
#     data = get_health_effects_file()
#     print(data)
#     final_ingredients['Health Effect'] = "NA"
#     print(final_ingredients)
#     for component in final_ingredients:
#         print(component)
#         if component in data['orig_compound_name'].values:
#             final_ingredients['Health Effect'][component] = result[result['orig_compound_name'] == component].values[0][1]
#     return final_ingredients

# import pandas as pd
# import re

# def get_health_effects_file():
#     file_path = r"src/data/CompoundsHealthEffect.xlsx"
#     sheet_name = 'CompoundsHealthEffect'
#     data = pd.read_excel(file_path, sheet_name=sheet_name)
#     columns_of_interest = ['orig_compound_name', 'orig_health_effect_name']
#     data = data[columns_of_interest]
#     result = data.groupby('orig_compound_name')['orig_health_effect_name'].agg(concatenate_health_effects).reset_index()
#     result_indexed = result.set_index('Name', drop=False)
#     final_result.index = result_indexed.index.str.lower()
#     return final_result

# def concatenate_health_effects(series):
#     return ', '.join(series)

# def found_in_db(final_ingredients):
#     result = get_health_effects_file()
#     final_ingredients['Health Effect'] = "NA"
#     for component in final_ingredients.index:
#         print(f"Searching for '{component}':")
#         search_item = r"\b" + re.escape(component.lower()) + r"\b"  # Use regex word boundaries
#         found_items = results[results.index.str.contains(search_item, case=False, na=False, regex=True)]

#         if not found_items.empty:
#             final_ingredients.at[component, 'Health Effect'] = found_items['orig_health_effect_name'].values[0]
            
#         else:
#             print("No items found matching the search criteria for", component)
#         print("\n")
        
#         # if component in result['orig_compound_name'].values:
#         #     final_ingredients.at[component, 'Health Effect'] = result[result['orig_compound_name'] == component]['orig_health_effect_name'].values[0]
#     return final_ingredients

import pandas as pd
import re

def get_health_effects_file():
    file_path = r"src/data/CompoundsHealthEffect.xlsx"
    sheet_name = 'CompoundsHealthEffect'
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    columns_of_interest = ['orig_compound_name', 'orig_health_effect_name']
    data = data[columns_of_interest]
    result = data.groupby('orig_compound_name')['orig_health_effect_name'].agg(concatenate_health_effects).reset_index()
    result_indexed = result.set_index('orig_compound_name', drop=False)  # Set index to 'orig_compound_name'
    return result_indexed

def concatenate_health_effects(series):
    return ', '.join(series)

def found_in_db(final_ingredients):
    results = get_health_effects_file()  # Rename 'result' to 'results' to match the variable name
    final_ingredients['Health Effect'] = "NA"
    for component in final_ingredients.index:
        print(f"Searching for '{component}':")
        search_item = r"\b" + re.escape(component.lower()) + r"\b"  # Use regex word boundaries
        found_items = results[results.index.str.contains(search_item, case=False, na=False, regex=True)]

        if not found_items.empty:
            final_ingredients.at[component, 'Health Effect'] = found_items['orig_health_effect_name'].values[0]
            
        else:
            print("No items found matching the search criteria for", component)
        print("\n")
    return final_ingredients

# Example usage:
# df = found_in_db(df)
