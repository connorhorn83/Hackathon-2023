# import pandas as pd
# import re
# from ComponentGeneralUse_Dataparse import search_components

# def concatenate_health_effects(series):
#     return ', '.join(series)

# file_path = r"src/data/CompoundsHealthEffect.xlsx"
# sheet_name = 'CompoundsHealthEffect'
# data = pd.read_excel(file_path, sheet_name=sheet_name)
# columns_of_interest = ['orig_compound_name', 'orig_health_effect_name']
# data = data[columns_of_interest]
# result = data.groupby('orig_compound_name')['orig_health_effect_name'].agg(concatenate_health_effects).reset_index()

# element = result.loc[result['orig_compound_name'] == 'CAFFEINE', 'orig_health_effect_name'].values[0]

# temp = ['caffeine']
# dataframe = pd.DataFrame()
# dataframe = search_components(temp)
# dataframe['Health Effect'] = "NA"
# print(dataframe)

# indexed_data = result.set_index('orig_components_name', drop=False)
# indexed_data.index = indexed_data.index.str.lower()


# for component in dataframe['Name']:
#     print(f"Searching for '{component}':")
#     search_item = r"\b" + re.escape(component.lower()) + r"\b"  # Use regex word boundaries
#     found_items = indexed_data[indexed_data.index.str.contains(search_item, case=False, na=False, regex=True)]

