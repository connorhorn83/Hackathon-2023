from taipy import Gui
from webcam import Webcam
from data.ComponentGeneralUse_Dataparse import search_components

test_list = ['Biotin', ' ascorbic acid', 'pantothenic']

df = search_components(test_list)

url = None
# TODO: figure out the fuckin picture
page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' to get nutritional information about the food.

<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
<|Analyze|button|on_action=analyze|>

<|{url}|image|>

<|{df}|table|>

"""

def analyze(state):
    # anaylyze shit
    pass
          
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")