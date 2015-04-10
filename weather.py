import urllib2
import json
import requests
import re


def get_current_temp_f():

	#f = urllib2.urlopen("http://api.wunderground.com/api/5fca88677185ab39/conditions/q/CA/San_Francisco.json")
	f = urllib2.urlopen('http://api.wunderground.com/api/5fca88677185ab39/geolookup/conditions/q/IA/Singapore.json')
	json_string = f.read()

	#print json_string

	parsed_json = json.loads(json_string)
	location = parsed_json['location']['city']
	temp_f = parsed_json['current_observation']['temp_f']

	print "Current Temperature in %s is %s" % (location, temp_f)

	f.close()
	
#get_current_temp_f()


def get_weather_forcast(country, city):
	key   = '5fca88677185ab39'
	urlp1 = 'http://api.wunderground.com/api'
	url = "%s/%s/forecast/q/%s/%s.json"%(urlp1,key,country,city)
	print url
	
	r = requests.get(url)
	data = r.json()
	#print data['forecast']['simpleforecast']['forecastday']
	for day in data['forecast']['simpleforecast']['forecastday']:
		print day['date']['weekday'] + ':'
		print "Conditions: ",day['conditions']
		print "High: ",day['high']['celsius'] + "C",
		print "Low : ",day['low']['celsius'] + "C", "\n"
	
def get_external_ip():
        url = "http://checkip.dyndns.org"
        f = urllib2.urlopen(url)
        request = f.read()
        print request
        theIP = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
        print theIP.group()

        return theIP.group() if theIP else None
get_external_ip()


#get_weather_forcast('France', 'Paris')








