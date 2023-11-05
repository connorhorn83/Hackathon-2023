from taipy import Gui
from data.ComponentGeneralUse_Dataparse import search_components

test_list = ['Biotin', ' ascorbic acid', 'pantothenic']

df = search_components(test_list)
queryInput = ""
url = None
# TODO: figure out the fuckin picture
page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' to get nutritional information about the food.

<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
<|Analyze|button|on_action=analyze|>
<|{queryInput}|input|label=Search...|>

<|{df}|table|filter=True|>

"""
def on_change(state, var_name, var_value):
    if var_name == "queryInput":
        state.queryInput = ''
        print(queryInput)
        return
        
def analyze(state):
    # anaylyze shit
    pass
          
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")