"""
This is a short script to search for local places to ride and
provide weekend weather for the local trail selected.
"""
import yaml
from helper import where_is_you, get_trails, get_weather

# importing config to access values
with open("config.yaml", 'r') as yamlfile:
    cfg = yaml.safe_load(yamlfile)

# values
weatherauth = (cfg['darksky']['apikey'])
mtbauth = (cfg['mtbproject']['apikey'])
zipcode = (cfg['profile']['zipcode'])

# If location is not available for ease of access later
# ~~~~~~~ NEED TO COMPLETE THIS FUNCTION so it writes zipcode, lat & long to config.yaml file  ~~~~~~~
if zipcode is None:
    where_is_you()

# values from zip code
lat = (cfg['profile']['latitude'])
long = (cfg['profile']['longitude'])
dist = (cfg['profile']['distance'])

# getting trails based on your latitude, longitude, preferred distance
trails = get_trails(lat, long, dist, mtbauth).get('trails')
# list of trails

local_trails = []
trail_locations = []

# removing duplicate trail locations
for trail in trails:
    if trail['location'] not in trail_locations:
        local_trails.append(trail)
        trail_locations.append(trail['location'])
    print(trail['name'], " - ", trail['location'])

print(local_trails)

"""
print(get_trails(lat, long, dist, mtbauth))
print('=================================')

weather = get_weather(weatherauth, lat, long)
print(weather)
type(weather)
"""