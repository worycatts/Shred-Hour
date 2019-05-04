"""
This is a short script to search for local places to ride and
provide weekend weather for the local trail selected.
"""
import urllib3


http = urllib3.PoolManager()
r = http.request('GET', 'https://www.mtbproject.com/data/get-trails?lat=LAT&lon=LONG&maxDistance=60&key=auth')
