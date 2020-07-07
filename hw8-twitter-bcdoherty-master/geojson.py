import urllib.request, urllib.parse, urllib.error
import json

# Google requires a key for this API - you can create a key but you need to
# give a credit card.  You get $300 credit.  See http://g.co/dev/maps-no-account
# Pick Places (Geolocation API)
# Enter the key below after key=
serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?key='

while True:
    address = input('Enter location like Ann Arbor, MI: ')
    if len(address) < 1: break

    url = serviceurl + "&" + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print the json as an indented string
    print(json.dumps(js, indent=4))

    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']

    # print(country)
    #print(js)
    #country = js["results"][0]["address_components"]
    #for d in country:
    #    if 'country' in d["types"]:
    #        print(d["short_name"])
