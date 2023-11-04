from taipy import Gui

url = None
# TODO: figure out the fuckin picture
page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' to get nutritional information about the food.

<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
<|Analyze|button|on_action=analyze|>

"""

def analyze(state):
    # anaylyze shit
    pass
          
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")