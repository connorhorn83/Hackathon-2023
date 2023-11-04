from taipy import Gui
from webcam import Webcam

url = None
# TODO: figure out the fuckin picture
page = """

# Nutri*py*
Upload an image of your 'Nutrition Facts' to get nutritional information about the food.

<|{url}|file_selector|label=Upload Image|extensions=".raw,.jpeg,.png,.jpg"|>
<|Analyze|button|on_action=analyze|>
<|Capture photo|button|on_action=capture|>

<|{url}|image|>
"""

def capture(state):
    pass

def analyze(state):
    # anaylyze shit
    pass
          
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")