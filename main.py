from pathfinder import get_stops_near_location
from data_builder import search_for_routes

def main():
  print("This program can tell you the public transit stops near a location in NY (and potentially more in the future)")
  print("Enter the coordinates below (If you're not sure of the coordinates try using this link: https://www.latlong.net/convert-address-to-lat-long.html)")
  user_lat = float(input("Enter the lattitude: "))
  user_lon = float(input("Enter the longitude: "))
  print("Enter how far you're willing to travel to a public transit stop (in meters). Keep in mind if you would theoretically be walking, riding a bike or car over, or getting dropped off")
  user_radius = float(input("Enter the distance: "))
  search_for_routes(user_lat,user_lon,user_radius)
  get_stops_near_location(user_lat,user_lon,user_radius)

main()