#module to query Google Maps API and find distance in miles between legs of a trip, and then sum all legs of the trip
#takes input list of 2 cities preferable in format topeka, ks (case not relevant)

from google.directions import GoogleDirections
import time

gmaps = GoogleDirections('AIzaSyCSvWGbxjEQw4jfQzrquRf4QTcrsD9wb9w')#your Google Maps API key

def state_fix(city):
	#appends state: ar to cities input without state

	if city == '':
		return city	
	if city == None:
		return city
	if len(city.split(',')) == 1:
		city += ", ar"
		return city
	else:
		return city

def geocode_city(city_list):
	cleaned_list = []

	for city in city_list:
		cleaned_list.append(state_fix(city))

	return cleaned_list
	
def get_distance(geo_list):
	address1 = geo_list[0]
	address2 = geo_list[1]
	
	results = gmaps.query(address1, address2)
	leg_distance = int(round(results.distance / 1609.344)) #convert to miles
	
	return leg_distance
	
def main(raw_list):
	final_distance = get_distance(geocode_city(raw_list))
	return final_distance
	
