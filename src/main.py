from taipy import Gui
from data.ComponentGeneralUse_Dataparse import search_components, run_processing
import pandas as pd

# test_list = ['Biotin', ' ascorbic acid', 'pantothenic']
queryInput = ""
df = pd.DataFrame()

url = None
# TODO: figure out the picture
page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' to get nutritional information about the food.

<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
<|{queryInput}|input|label=Search...|>

<|{url}|image|>
<|{df}|table|filter|rebuild=True|>
"""

def on_change(state, var_name, var_value):
    if var_name == "queryInput":
        queryInputSearch = var_value
        queryList = [queryInputSearch]
        df2 = search_components(queryList)
        page = """

        # Nutri*py*
        Upload an image of your 'Nutrition Facts' to get nutritional information about the food.

        <|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
        <|{queryInput}|input|label=Search...|>

        <|{url}|image|>
        <|{df}|table|filter|rebuild=True|>
        """

    elif var_name == "url":
        url2 = var_value
        print(url2)
        df = run_processing(url2)

Gui(page=page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")