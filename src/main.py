from taipy import Gui
from data.ComponentGeneralUse_Dataparse import search_components
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
<|Analyze|button|on_action=analyze|>
<|{queryInput}|input|label=Search...|>

<|{df}|table|filter|rebuild|>

"""

def on_change(state, var_name, var_value):
    if var_name == "queryInput":
        queryInputSearch = var_value
        queryList = [queryInputSearch]
        df = search_components(queryList)
        
def analyze(state):
    queryList = [queryInput]
    df = search_components(queryList)

Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")