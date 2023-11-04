from taipy import Gui

img = 0
renderResults = False
    
page = """

# Nutri*py*
## Upload your image here.

<|{img}|file_selector|extensions=".raw,.jpeg,.png,.jpg"|>
<|Analyze|button|on_action={lambda s: s.assign("renderResults", True)}}|>
<|test|part|render={renderResults}|>

"""
    
    
Gui(page).run(use_reloader=True,  title="Nutripy", favicon="img/nutrition.ico")