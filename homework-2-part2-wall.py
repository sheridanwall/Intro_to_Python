# Sheridan Wall
# Nov. 1, 2020
# Homework 2, Part 2


# Part Two: Lists
countries = ['italy' , 'romania' , 'portugal' , 'armenia' , 'russia' , 'ghana' , 'india']
for country in countries:
    print(country)

# Sort permanentyl
countries.sort()
print(countries)

# display first element
print(countries[0])
# Armenia

# display second-to-last
print(countries[5])
# Romania

# delete country from list with name
countries.remove('russia')
print(countries)

# w/ for loop, print all country names in caps
for country in countries:
    country = country.upper()
    print(country)

#Part Two: Dictionaries
trees = {
    'name' : 'Cypress of Abarkuh' ,
    'species' : 'Cupressus sempervirens' ,
    'age' : 4500 ,
    'location_name' : 'Abarkuh, Iran' ,
    'latitude' : 31.1226 ,
    'longitude' : 53.2798 ,
}
print(trees['name'] , "is a" , trees['age'] , "year old tree that is in" , trees['location_name'])

# NYC lat = 40.7128° N 
nyc_lat = 40.7128
if nyc_lat > trees['latitude'] :
    print("The tree" , trees['name'] , "in" , trees['location_name'] , "is south of NYC")
elif nyc_lat < trees['latitude'] :
    print("The tree" , trees['name'] , "in" , trees['location_name'] , "is north of NYC")

# User age comparison
age = int(input("How old are you?"))
if age > trees['age']:
    print("You are" , age - trees['age'], "than" , trees['name'])
elif age < trees['age']:
    print(trees['name'] , "was" , trees['age'] - age , "years old when you were born")

#Part Two : Lists of dictionaries --> stack overflow
places = [
    {
        'city' : 'Moscow' , 
        'latitude' : 55.7616 , 
        'longitude' : 37.6095
        },
    {
        'city' : 'Tehran' ,
        'latitude' : 35.6682, 
        'longitude' : 51.3744
        },
    {
        'city' : 'Falkland Islands' ,
        'latitude' : -51.7967, 
        'longitude' : -58.5949
        },
    {
        'city' : 'Seoul' ,
        'latitude' : 37.5479, 
        'longitude' : 126.9419
        },
    {
        'city' : 'Santiago' ,
        'latitude' : -33.4450, 
        'longitude' : -70.6671
        }
]
for place in places:
    print(place['city'])
    if place['latitude'] > 0:
        print("is above the equator")
    elif place['latitude'] < 0:
        print("is below the equator")
    if place['city'] == 'Falkland Islands':
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone")
    if place['latitude'] > trees['latitude']:
        print("and north of my tree")
    elif place['latitude'] < trees['latitude']:
        print("and south of my tree")












