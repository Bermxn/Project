import questionary

#region Name 
_name = questionary.text("Enter your name for the order", validate= any).ask()
#endregion

#region Size
_size = questionary.select(
    "What size would you like?",
    choices=[
        "Junior (4-inch)",
        "Shorti (6-inch)",
        "Classic (10-inch)"
    ], instruction = 'Use Arrow Keys').ask()
#endregion

#region Spread
_spread = questionary.select(
    "What spread would you like?",
    choices=[
        "None",
        "Mustard",
        "Mayo",
        "Ranch",
        "Vingear"
    ], instruction = 'Use Arrow Keys').ask()
#endregion

#region Toppings
_toppings = questionary.checkbox(
   'Select Toppings',
    choices=[
       "Cheese",
       "Tomato",
       "Lettuce",
       "Onion",
       "Oregano",
       "Pickles"
    ]).ask()
#endregion

#region Extras
_extras = questionary.checkbox(
   'Select Extras',
    choices=[
       "Bacon",
       "Extra Meat",
       "Sardines",
       "Olives",
       "Peppers",
       "Pepperoncini"
    ]).ask()
#endregion

#region Sides
_sides = questionary.checkbox(
   'Select Sides',
    choices=[
       "Tea",
       "Water",
       "Cookie",
       "Fruit Cup",
       "Chips"
    ]).ask()
#endregion

#region Methods
def Calculate_Tip():
    while True:
        try:
            tip = int(questionary.text("Enter a tip (ex: 10 = 10%)", validate= any).ask())
            if tip in range(0,2147483647):
                return (tip/100)
                break
        except ValueError:
            print ("Only positive whole numbers are allowed")
            continue

def Determine_Sandwich_Size_Price():
    if _size == "Junior (4-inch)":
        return 3.99
    elif _size == "Shorti (6-inch)":
        return 4.99
    else:
        return 5.99

def Determine_Extras_Price():
    price = 0.00
    for x in _extras:
        price += 1.99
    return price

def Determine_Sizes_Price():
    price = 0.00
    for x in _sides:
        if x == 'Tea' or x == 'Water':
            price += 1.99
        elif x == 'Cookie':
            price += 1.25
        elif x == 'Chips':
            price += 0.99
        elif x == 'Fruit Cup':
            price += 2.99
        else:
            price += 0.00
    return float(price)
#endregion

#region Pricing
_sizePrice = Determine_Sandwich_Size_Price()
_extrasPrice = Determine_Extras_Price()
_sidesPrice = Determine_Sizes_Price()   
_subtotal = _sizePrice + _extrasPrice + _sidesPrice
_tip = "{:.2f}".format(Calculate_Tip() * _subtotal)
_total = "{:.2f}".format(float(_subtotal) + float(_tip))
print ("\nOrder Summary\nSubtotal: $" + str(_subtotal) + "\nTip: $" + str(_tip) + "\nTotal: $" + str(_total))
#endregion

