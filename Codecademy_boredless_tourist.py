print('Lets get started with the Codecademy Boredless Tourist project')

destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

#print(test_destination_index)

attractions = [[] for i in destinations]
#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions[destination_index].append(attraction)
  except ValueError:
    return
  
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])  

print(attractions)

