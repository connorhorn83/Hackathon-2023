from taipy import Gui
from taipy.gui import Html

img = 0
renderResults = None

def handleClick(state):
    pass

page = """

# Nutri*py*
## Upload your image here.

<|{img}|file_selector|extensions=".raw,.jpeg,.png,.jpg"|>
<|Analyze|button|on_action=handleClick|>
Render Results: <|{renderResults}|text|>

"""
    
Gui(page).run(use_reloader=True, title="Nutripy", favicon="img/nutrition.ico")