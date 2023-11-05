from taipy import Gui
from data.ComponentGeneralUse_Dataparse import search_components, run_processing, run_intake
import pandas as pd

queryInput = ""
df = pd.DataFrame()
dfimg = pd.DataFrame()
url = None

page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' or enter an ingredient into the search bar to get nutritional information, a summary, and advisories about daily intakes about the food.

<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
<|{queryInput}|input|label=Search...|>

<|{df}|table|filter|rebuild=True|>
## Daily Intakes
<|{dfimg}|table|filter|rebuild=True|>
"""

def on_change(state, var_name, var_value):
    if var_name == "queryInput":
        if var_value != "" or " ":
            queryInputSearch = var_value
            queryList = [queryInputSearch]
            state.df = pd.DataFrame()
            state.df = search_components(queryList)

    elif var_name == "url":
        url2 = var_value
        print(url2)
        state.df = pd.DataFrame()
        state.dfimg = pd.DataFrame()
        state.df = run_processing(url2)
        state.dfimg = run_intake(url2)
        

Gui(page=page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")