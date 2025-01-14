# Initialize
dict1 = {'name':'taz', 'age' : 25 , 'occupation': "Software Developer"}
# Adding
dict1["country"] = 'Sudan'
print(dict1)
# Edit
dict1["name"] = 'Tazy'
print(dict1)
# Removing
del dict1["name"] 
print(dict1)
# Looping
for (_,v) in dict1.items() :
    print(v)
# Nesting
capitals = {
    'France':'Paris',
    'Germany':'Berlin'
}
travel_log = {
    'France': ["Paris","Lille",'Lyon'],
    'Gernmany': ["Berlin","Bochum",'Frankfurt']
}
travel_log2 = {
    'France': {'cities_visted': ["Paris","Lille",'Lyon'], 'total_visits':12},
    'Gernmany': {'cities_visted': ["Berlin","Bochum",'Frankfurt'], 'total_visits':5}
}
print(capitals,travel_log,travel_log2)

# Clear
dict1.clear()
print(dict1)
