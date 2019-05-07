import json
import urllib3
import yaml
from uszipcode import SearchEngine



def read_config(data):
    with open('config.yml', 'r') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    outfile.close()


def write_config(data):
    with open('config.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    outfile.close()


def get_zipcode_data(zipcode):
    # set simple_zipcode=False to use rich info database
    search = SearchEngine(simple_zipcode=True)
    data = search.by_zipcode(str(zipcode))
    return data


# ~~~~~~~ NEED TO COMPLETE THIS FUNCTION so it writes zipcode, lat & long to config.yaml file  ~~~~~~~
def where_is_you():
    # requesting zipcode data to find your location in relation to the trails!
    return get_zipcode_data(input("Looks like we don't know where you are. "
                                  "Please enter your zipcode to provide reference: "))


def get_trails(lat, long, dist, mtb_auth):
    http = urllib3.PoolManager()
    url = http.request('GET', 'https://www.mtbproject.com/data/get-trails?lat=%s&lon=%s&maxDistance=%s&key=%s'
                       % (lat, long, dist, mtb_auth))
    data = json.loads(url.data.decode('utf-8'))
    return data


def get_weather(weather_auth, lat, long):
    http = urllib3.PoolManager()
    return http.request('GET', "https://api.darksky.net/forecast/%s/%s,%s" % (weather_auth, lat, long))


def remove_duplicates(list_of_trails):
    # removing duplicate trail locations
    local_trails = []
    trail_locations = []

    # loops thru trails
    for trail in list_of_trails:
        # compares trail['location'] to list of trail | if trail exists in trails, don't add it again
        if trail.get('location') not in trail_locations:
            local_trails.append(trail)
            trail_locations.append(trail.get('location'))

    return local_trails


