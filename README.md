# Hackathon-2023
Make UC Hackathon team: Connor Horn, Logan Muhlen, Lucas Fox, Cameran Beason.

## Introducing Nutri*py*
Nutripy is a web application that helps to inform users about the nutritional contents of their food and beverages. Ingredients are identified and quickly summarized, all from one picture of the product's barcode. Nutripy is a great tool for those who want to be more informed about what they are eating, and for those who want to make healthier choices.

## How Nutripy works

#### Home Page:
Here you have the choice of inputting an image or searching for a specific ingredient.
<p><img src="https://github.com/connorhorn83/Hackathon-2023/assets/100247149/8478eedc-1e10-44b8-92c0-f62e14cd2589" alt="Home Page" style="border:1px solid black; width:70%;"></p>

#### Inputting Image:
I have selected to input the image below into the app.
<p><img src="https://github.com/connorhorn83/Hackathon-2023/assets/100247149/a072c3d2-2614-423a-88f0-1ce2abe1eb11" alt="Home Page" style="border:1px solid black; width:70%;"></p>

#### Barcode Scanning:
Once your image has be entered into the app, the barcode will be scanned and decoded using the pyzbar Python package. From here, the decoded barcode will be used to call the barcodelookup API which returns information based on the barcode. The nutrition facts and ingredients are then pulled from what is returned by the API call and used to generate the app's two tables.

#### Ingredients Table:
The ingredients table houses the food or drink item's ingredients and the ingredients uses (From FoodSubstances.xlsx), potential health effects (From CompoundsHealthEffect.xlsx), and a summmary which is pulled from Wikipedia using the wikipedia Python package.
<p><img src="https://github.com/connorhorn83/Hackathon-2023/assets/100247149/1146aee4-221d-4f47-995c-3c5385625308" alt="Home Page" style="border:1px solid black; width:70%;"></p>

#### Daily Intakes Table:
The daily intakes table contains estimations of how much the food or drink product contributes to the average recommended daily intake of various important nutrition categories. The methodology behind this estimation requires more testing and experimentation to be relied on fully due to the 24-hour time contraints of the hackathon.
<p><img src="https://github.com/connorhorn83/Hackathon-2023/assets/100247149/f42dbb8d-14ab-47dc-b2d2-3b25ee2454a7" alt="Home Page" style="border:1px solid black; width:70%;"></p>

#### Search Feature:
The search feature allows for specific ingredients to be searched rather than inputting an entire food or drink's barcode.
<p><img src="https://github.com/connorhorn83/Hackathon-2023/assets/100247149/a87e8874-7113-4cc9-8544-dac275d2e664" alt="Home Page" style="border:1px solid black; width:70%;"></p>

## Area's For Improvement
- We'd like to first improve on the methodology behind the daily intakes table to ensure the estimations are reliable for users.
- Next we'd work on improving the UI to make Nutripy more user friendly. One way we'd do this is by adding helper buttons that pop up information to the user over where information is pulled from so that there is full transparency with the user on where what they are seeing is coming from.
- We could then continue improving our barcode scanning reliability by testing and accounting for cases where the inputted image has an unclear barcode.
- Later down the road, we'd like to add the feature to take a picture within the app to streamline this image input process.
