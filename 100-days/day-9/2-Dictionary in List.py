travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# TODO: Escreva a função que permitirá novos países
# to be added to the travel_log. 👇


def add_new_country(pais, visitas, cidades):
    new_country = {}
    new_country["country"] = pais
    new_country["visits"] = visitas
    new_country["cities"] = cidades
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

add_new_country("United States", 3, [
                "United States", "New York", "Washington"])

add_new_country("Brazil", 4, ["São Paulo", "Rio de Janeiro", "Brasília"])
print(travel_log)
