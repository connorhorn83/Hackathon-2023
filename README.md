# Hackathon-2023
Make UC Hackathon team: Connor Horn, Logan Muhlen, Lucas Fox, Cameran Beason.

## Introducing Nutri*py*
Nutripy is a web application that helps to inform users about the nutritional contents of their food and beverages. Ingredients are identified and quickly summarized, all from one picture of the product's barcode. Nutripy is a great tool for those who want to be more informed about what they are eating, and for those who want to make healthier choices.

## How Nutripy works

#### Home Page
Here you have the choice of inputting an image or searching for a specific ingredient.
![image](https://github.com/connorhorn83/Hackathon-2023/assets/100247149/8478eedc-1e10-44b8-92c0-f62e14cd2589)

#### Inputting Image
I have selected to input the image below into the app.
![Smokehouse_BBQ](https://github.com/connorhorn83/Hackathon-2023/assets/100247149/a072c3d2-2614-423a-88f0-1ce2abe1eb11)

#### Barcode Scanning
Once your image has be entered into the app, the barcode will be scanned and decoded using the pyzbar Python package. From here, the decoded barcode will be used to call the barcodelookup API which returns information based on the barcode. The nutrition facts and ingredients are then pulled from what is returned by the API call and used to generate the app's two tables.

#### Ingredients Table
The ingredients table houses the food or drink item's ingredients and the ingredients uses (From FoodSubstances.xlsx), potential health effects (From CompoundsHealthEffect.xlsx), and a summmary which is pulled from Wikipedia using the wikipedia Python package.
![image](https://github.com/connorhorn83/Hackathon-2023/assets/100247149/1146aee4-221d-4f47-995c-3c5385625308)

#### Daily Intakes Table

![image](https://github.com/connorhorn83/Hackathon-2023/assets/100247149/f42dbb8d-14ab-47dc-b2d2-3b25ee2454a7)

#### Search Feature
![image](https://github.com/connorhorn83/Hackathon-2023/assets/100247149/a87e8874-7113-4cc9-8544-dac275d2e664)


## Area's For Improvement


## Takeaways
