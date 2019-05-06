import yaml
from uszipcode import SearchEngine


def get_zipcode_data(zipcode):
    search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
    data = search.by_zipcode(str(zipcode))
    return data

def write_config(data):
    with open('config.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    outfile.close()

def read_config(data):
    with open('config.yml', 'r') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    outfile.close()


