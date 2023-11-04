from taipy import Gui

url = None
# TODO: figure out the fuckin picture
page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' to get nutritional information about the food.
<br></br>
<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg,.raw"|>
<|Analyze|button|on_action=analyze|>
<br></br>
<|{url}|image|>
"""

def capture(state):
    pass

def analyze(state):
    # anaylyze shit
    pass
          
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")