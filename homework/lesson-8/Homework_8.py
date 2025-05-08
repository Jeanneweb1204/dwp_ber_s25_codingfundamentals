european_cities = [
    ("Istanbul", [15460000, "Kebab", "Hagia Sophia"]),
    ("Moscow", [12678079, "Borscht", "Red Square"]),
    ("London", [8982000, "Fish and Chips", "Big Ben"]),
    ("St. Petersburg", [5383890, "Blini", "Hermitage Museum"]),
    ("Berlin", [3669491, "Currywurst", "Brandenburg Gate"]),
    ("Madrid", [3348536, "Paella", "Royal Palace of Madrid"]),
    ("Kiev", [2884000, "Borscht", "Saint Sophia's Cathedral"]),
    ("Paris", [2140526, "Croissant", "Eiffel Tower"])
]
european_cities_info = {city: info for city, info in european_cities}
print("💚 City Information:")
for city, info in european_cities_info.items():
    print(f"{city} --> {info}")
print("💚 \nAlphabetically Sorted City Info:")
sorted_cities = sorted(european_cities_info) 

for city in sorted_cities:
    info = european_cities_info[city]        
    print(f"{city} --> {info}")
berlin_info = european_cities_info.get("Berlin", "Not Found") 
print("\nBerlin:", berlin_info)
london_info = european_cities_info.get("London")  
print("London info:", london_info)                
print("Type of London info:", type(london_info))
european_cities_info["Rome"] = [2870500, "Pasta", "Colosseum"]
print("Added Rome:", european_cities_info["Rome"])
removed_madrid = european_cities_info.pop("Madrid", None)
if removed_madrid:
    print("Removed Madrid:", removed_madrid)
else:
    print("Madrid not found")
if "Amsterdam" in european_cities_info:
    print("Amsterdam is in the dictionary.")
else:
    print("Amsterdam is NOT in the dictionary.")
dishes = ["Pizza", "Sauerkraut", "Paella", "Hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_dishes = {}
for i in range(len(countries)):
    country = countries[i]
    dish = dishes[i]
    country_dishes[country] = dish 
print("\nCountry Dishes Dictionary:", country_dishes)
