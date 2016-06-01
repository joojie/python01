
import urllib
import json


serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
#serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('\nEnter a location: ')
    if len(address) < 1 : break

    print 'Retrieving',  serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieved',len(urllib.urlopen( serviceurl + urllib.urlencode({'sensor':'false', 'address': address})).read()),'characters'

    try: js = json.loads(urllib.urlopen( serviceurl + urllib.urlencode({'sensor':'false', 'address': address})).read())
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        continue

    place_id = js["results"][0]["place_id"]
    print 'Place id', place_id