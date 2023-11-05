import pandas as pd

def concatenate_health_effects(series):
    return ', '.join(series)

def get_he_data():
    # set up variables
    file_path = r"src/data/CompoundsHealthEffect.xlsx"
    sheet_name = 'CompoundsHealthEffect'
    columns_of_interest = ['orig_compound_name', 'orig_health_effect_name',]

    # pull data, take only wanted columns and change column names
    he_data = pd.read_excel(file_path, sheet_name=sheet_name)
    he_data = he_data[columns_of_interest]
    he_data = he_data.rename(columns={'orig_compound_name': 'Name', 'orig_health_effect_name': 'Health Effects'})
    
    # drop duplicates and send all to lowercase
    he_data = he_data.drop_duplicates()
    he_data['Name'] = he_data['Name'].str.lower().str.strip()

    # group by name and concatenate health effects
    he_data = he_data.groupby('Name')['Health Effects'].agg(concatenate_health_effects).reset_index()

    return he_data