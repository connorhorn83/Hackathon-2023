from taipy import Gui

img = 0
renderResults = False
page = """

# Nutrify
## Upload your image *here*.

<|{img}|file_selector|extensions=".raw,.jpeg,.png,.jpg"|>
<|Analyze|button|on_action=handleAnalysis|>
"""

def handleAnalysis(state):
    print(f"Analyzed.")
    renderResults = True
    
    
Gui(page).run(use_reloader=True, title="Nutrify", favicon="img/nutrition.ico")