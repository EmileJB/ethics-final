# preliminary final project
import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token='geA6qNwvpHVBEDAVXq33qNDOb')
print("")


print("bikes in building")
bikes_in_buildings = client.get("scjj-6yaf", select = 'tenantpostcode, noofbicyclerequested, requeststatus, council_district, census_tract, nta', limit = 50000) #not sure if all of these are necessary

print(bikes_in_buildings)



print("ramp lift usage")

ramp_lift_usage = client.get("e2u6-bmnn", limit = 50000) 
print (ramp_lift_usage)


bus_service_delivered = client.get("2e6s-9gpm", limit = 50000) 


mta_daily_ridership = client.get("vxuj-8kew", limit = 50000)

