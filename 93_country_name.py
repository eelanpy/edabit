# 93_country_name:
guests = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}


def name_country(name):
    greeting = ""
    if name in guests.keys():
        greeting = "Hi! I'm {}, and I'm from {}.".format(name,guests[name])
    else:
        greeting = "Hi! I'm a guest."

    return greeting
        

print(name_country("Randy") )
assert name_country("Randy") == "Hi! I'm Randy, and I'm from Germany."

print(name_country("Sam"))
assert name_country("Sam") == "Hi! I'm Sam, and I'm from Argentina."

print(name_country("Monti"))
assert name_country("Monti") == "Hi! I'm a guest."