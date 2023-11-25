import pandas as pd
import operator
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token='geA6qNwvpHVBEDAVXq33qNDOb')
print("")



bikes_in_buildings = client.get("scjj-6yaf", select = 'noofbicyclerequested, ownerzipcode', limit = 50000) #not sure if all of these are necessary

#print(bikes_in_buildings)
#find the areas with the most requests


zip_codes = {}

for entry in bikes_in_buildings:
    if entry['ownerzipcode'] not in zip_codes:      #traverse through entire list of entries and add zip codes to dictionary while counting the entries for each zip code
        zip_codes[entry['ownerzipcode']] = 1
    else:
        zip_codes[entry['ownerzipcode']] += 1

# print(zip_codes) #this is a dictionary with the zip codes and the number of requests for each one
sorted_zip_codes = dict( sorted(zip_codes.items(), key=operator.itemgetter(1), reverse=True)) #sorts by descending values. found the solution online: https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php


print('Dictionary in descending order by value : ', sorted_zip_codes)




print("ramp lift usage")

ramp_lift_usage = client.get("e2u6-bmnn", limit = 50000) 
print (ramp_lift_usage)


bus_service_delivered = client.get("2e6s-9gpm", limit = 50000) 


mta_daily_ridership = client.get("vxuj-8kew", limit = 50000)

