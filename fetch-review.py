#Program to fetch Google reviews of a place using Google Places API

import requests
import json

place = input("Enter place name: ")

# replace the value for the parameter key with your API key
placeId = requests.get('https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input='+place+'&inputtype=textquery&fields=place_id,photos,formatted_address,name,rating,opening_hours,geometry&key=YOUR_API_KEY')

idJsonText = placeId.text
idText = json.loads(idJsonText)

place_id = idText['candidates'][0]['place_id']

# replace the value for the parameter key with your API key
placeDetails = requests.get('https://maps.googleapis.com/maps/api/place/details/json?place_id='+place_id+'&fields=name,rating,reviews&key=YOUR_API_KEY')


jsonText = placeDetails.text
text = json.loads(jsonText)
text

revList = text['result']['reviews']

fullReview = ""
for rev in revList:
  review = rev['text']
  fullReview = fullReview + review
print(fullReview)
