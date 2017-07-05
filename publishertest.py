from google.cloud import pubsub
import json, urllib

try:
    """with open('earthquakes.json', 'r') as data_file:
        data = json.load(data_file)
       """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2017-07-01&endtime=2017-07-05"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    client = pubsub.Client()
    topic = client.topic('earthquake-topic')
    
    numOfFeatures = len(data["features"])
    for x in range(0,numOfFeatures):
        eqtitle = data["features"][x]["properties"]["title"]
        eqtype = data["features"][x]["properties"]["type"]
        eqmag = str(data["features"][x]["properties"]["mag"])
        topic.publish(eqtitle, type=eqtype, mag=eqmag)
except Exception as e: 
    print('Something went wrong')
    s = str(e)
    print(s)
