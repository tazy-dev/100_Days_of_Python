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
#🚨 Do NOT change the code above 
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests
def add_new_country (country:str, no_of_visits:int,cities_visited:list[str]):
    new_log = {}
    new_log["country"] = country
    new_log["visits"] = no_of_visits
    new_log["cities"] = cities_visited
    travel_log.append(new_log)
    print(f"You've visited {country} {no_of_visits} times.")
    print(f"You've been to {" and ".join(cities_visited)}.")






#🚨 Do NOT change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
 