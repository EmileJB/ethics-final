# preliminary final project
import pandas as pd
from sodapy import Socrata

client = Socrata("data.ny.gov", app_token='geA6qNwvpHVBEDAVXq33qNDOb')
print("")


bikes_in_buildings = client.get("scjj-6yaf", select = 'tenantpostcode, noofbicyclerequested, requeststatus, council_district, census_tract, nta', limit = 50000) #not sure if all of these are necessary

print(bikes_in_buildings)


