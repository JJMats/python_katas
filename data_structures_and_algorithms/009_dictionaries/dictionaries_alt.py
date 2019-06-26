"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# Problem 1
print(1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

# Problem 2
print(2)
asia_cities = []
for countries, cities in iter(locations['Asia'].items()):
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)

asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)