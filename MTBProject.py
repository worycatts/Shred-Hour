"""
This is a short script to search for local places to ride and
provide weekend weather for the local trail selected.
"""
import urllib3
import yaml
from helper import get_zipcode_data, write_config, read_config


with open("config.yaml", 'r') as yamlfile:
    cfg = yaml.safe_load(yamlfile)

weatherauth = (cfg['darksky']['apikey'])
mtbauth = (cfg['mtbproject']['apikey'])
zipcode = (cfg['profile']['zipcode'])


def where_is_you():
    if zipcode is None:
        # requesting zipcode data to find your location in relation to the trails!
        data = get_zipcode_data(input("Looks like we don't know where you are. "
                                      "Please enter your zipcode to provide reference: "))
        print(data)


where_is_you()
lat = (cfg['profile']['latitude'])
long = (cfg['profile']['longitude'])
dist = (cfg['profile']['distance'])

http = urllib3.PoolManager()
trails = http.request('GET', 'https://www.mtbproject.com/data/get-trails?lat=%s&lon=%s&maxDistance=%s&key=%s'
                      % (lat, long, dist, mtbauth))
print(trails.data)

forecast = http.request('GET', "https://api.darksky.net/forecast/%s/%s,%s" % (weatherauth, lat, long))

print(forecast.data)



