# Combining all previous assignments into one project
from pyscript import document

# Skills Test

non_metals = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.0026),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.90),
    "Xe": ("Xenon", 54, 131.29),
    "Rn": ("Radon", 86, 222),
    "At": ("Astatine", 85, 210),
    "Ts": ("Tennessine", 117, 294),
    "Og": ("Oganesson", 118, 294)
}


# checking element symbol
def get_element(e):

    # get input
    element1 = document.getElementById("input1").value.strip().title()

    # get element info using .get()
    result = non_metals.get(
        element1,
        ("Sorry, your element is not in our list.", "", "")
    )

    # display element info
    document.getElementById("output1").innerHTML = f"""
        <b>Element Symbol:</b> {element1}<br>
        <b>Element Name:</b> {result[0]}<br>
        <b>Atomic Number:</b> {result[1]}<br>
        <b>Atomic Mass:</b> {result[2]}
    """

    # Seatwork 1
from pyscript import display, document

def get_nickname(e):
    document.getElementById('output1').innerHTML = " "
    country_nicknames = {
        "philippines": "The Pearl of the Orient Seas",
        "singapore": "The Lion City",
        "vietnam": "The Land of the Ascending Dragon",
        "indonesia": "The Emerald of the Equator",
        "thailand": "The Land of Smiles",
        "malaysia": "The Land of Truly Asia",
        "cambodia": "The Kingdom of Wonder",
        "myanmar": "The Golden Land",
        "brunei": "The Abode of Peace",
        "laos": "The Land of a Million Elephants",
        "timor-leste": "The Land of the Rising Sun in South East Asia"
    }

    country = document.getElementById('country_input').value.lower()

    # message if nickname not valid
    nickname = country_nicknames.get(country, "Sorry, I don't have a nickname for that country.")

    display(f"Nickname: {nickname}", target='output1')

# Drill 2
def get_name(e):
    document.getElementById("div1").innerHTML = ''
    club_members = ['carina jimenez', 'nancy milante', 'daphne mariano', 'alyanna barlisan', 'aj darimbang', 'jm piansay']
    first_name = document.getElementById("fname").value.lower().strip()
    last_name = document.getElementById("lname").value.lower().strip()
    full_name = first_name + ' ' + last_name
    name_checker = full_name in club_members
    display_message = (
        f'Sorry {full_name}, your name is not on the list of members. Try again next year!',
        f'Congratulations {full_name}! You are now part of the Rainbow Catering Club.'
    )
    display(display_message[name_checker], target='div1')