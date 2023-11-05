from taipy import Gui
from data.ComponentGeneralUse_Dataparse import search_components

test_list = ['Biotin', ' ascorbic acid', 'pantothenic']

df = search_components(test_list)
queryInput = "2"
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
        
def analyze(state):
    # anaylyze shit
    print(queryInput)
    pass
          
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")