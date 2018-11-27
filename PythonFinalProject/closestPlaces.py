import googlemaps
import requests
from operator import itemgetter

gmaps = googlemaps.Client(key='AIzaSyAPEQRxa7Yg9LCWrRg6YUp5oPQEh6Kka30')

place1 = input("Enter the first place")
place2 = input("Enter the second place")

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=36+College+Ave,+Annville,+PA+17003&'
                        'key=AIzaSyAPEQRxa7Yg9LCWrRg6YUp5oPQEh6Kka30')

# get location info about current location using a HTTP GET request
json_resp = response.json()

# need to pass in The latitude/longitude value for which you wish to obtain the closest, human-readable address
places = gmaps.places(place1, json_resp['results'][0]['geometry']['location'], 80467.2)

# We need a list of starting addresses for distance_matrix method
originsList = []
for x in places["results"]:
    tempAddress = x["formatted_address"]
    originsList.append(tempAddress)


# we need a list of ending addresses for distance_matrix method
destinationList = []
places2 = gmaps.places(place2, json_resp['results'][0]['geometry']['location'], 80467.2)

for y in places2["results"]:
    tempAddress = y["formatted_address"]
    destinationList.append(tempAddress)

dictionary = {}

for start in originsList:
    # find distance between the current 'start' location and each destination address
    distances = gmaps.distance_matrix(start, destinationList)
    for i in range(0, len(distances["rows"][0]["elements"])):
        distance = int(distances["rows"][0]["elements"][i]["distance"]["value"])

        # Create a unique key for our dictionary
        durationKey = start + " / " + distances["destination_addresses"][i]

        # Save the distance between 'start' and a destination
        dictionary[durationKey] = distance

# Create variables to store one of the three origin, destination pairs
origin1 = ""
dest1 = ""
distance1 = ""

origin2 = ""
dest2 = ""
distance2 = ""

origin3 = ""
dest3 = ""
distance3 = ""


# sort the dictionary based on value
i = 0
for key, value in sorted(dictionary.items(), key=itemgetter(1)):
    # split up key into origin/destination
    if i == 0:
        origin1 = key.split("/")[0]
        dest1 = key.split("/")[1]
        distance1 = value
        i = i + 1
    elif i == 1:
        origin2 = key.split("/")[0]
        dest2 = key.split("/")[1]
        distance2 = value
        i = i + 1
    elif i == 2:
        origin3 = key.split("/")[0]
        dest3 = key.split("/")[1]
        distance3 = value
        i = i + 1

print()
print()

# print out the three pairs
print("The first address is a " + place1 + " and the second address is a " + place2)
print("ORIGIN 1: " + origin1 + " DESTINATION 1: " + dest1 + " DISTANCE: " + str(distance1))
print("ORIGIN 2: " + origin2 + " DESTINATION 2: " + dest2 + " DISTANCE: " + str(distance2))
print("ORIGIN 3: " + origin3 + " DESTINATION 3: " + dest3 + " DISTANCE: " + str(distance3))
