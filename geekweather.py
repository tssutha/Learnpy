# -*- coding: utf-8 -*-

import urllib2
import os
import re
import sys
import json
from shutil import copy
from optparse import OptionParser

HOME = os.path.expanduser('~')
BASE_DIR = os.path.join(HOME, 'Documents', '', '')

DEGREE_SYMBOL = u"\N{DEGREE SIGN}"


def shorten_text(text):
    return text.replace(' and', '\nand')


class Weather():
    def __init__(self):
        parser = OptionParser()
        parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="Verbose output.")
        parser.add_option("-t", "--test", dest="testing", action="store_true", default=False, help="This is just a test.")
        parser.add_option("-c", "--current", dest="current", action="store_true", default=False, help="Get current weather conditions.")
        parser.add_option("-l", "--location", dest="location", action="store_true", default=False, help="Get location for weather.")
        parser.add_option("-f", "--forecast", dest="forecast", action="store_true", default=False, help="Get forecast for weather.")
        parser.add_option("-z", "--current_forecast", dest="current_forecast", action="store_true", default=False, help="Get current forecast for weather.")

        self.options, args = parser.parse_args()

        self.verbose = self.options.verbose
        self.testing = self.options.testing

        APP_KEY = '5fca88677185ab39'
        self.CONDITIONS_URL = 'http://api.wunderground.com/api/%s/conditions/q/autoip.json?geo_ip=' % APP_KEY
        self.FORECAST_URL = 'http://api.wunderground.com/api/%s/forecast/q/autoip.json?geo_ip=' % APP_KEY

        # Pick F, C or both
        self.f_or_c = 'both'

        self.ip = self.get_external_ip()

        if not self.ip:
            sys.exit(1)

    def run_tasks(self):
    	
        #if self.options.current or self.options.location:
        self.conditions_data = self.get_conditions()
        #if self.options.location:
        self.location()
        #if self.options.current:
        self.current()
        #if self.options.forecast or self.options.current_forecast:
        self.forecast_data = self.get_forecast()
        #if self.options.forecast:
        self.forecast()
        #if self.options.current_forecast:
        self.current_forecast()

    def get_external_ip(self):
        url = "http://checkip.dyndns.org"
        f = urllib2.urlopen(url)
        request = f.read()
    	print request
        theIP = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", request)
		
        return theIP.group() if theIP else None

    def get_conditions(self):
        request = urllib2.urlopen(self.CONDITIONS_URL + self.ip).read()

        wjson = json.loads(request)
        obs = wjson['current_observation']
        return obs

    def get_forecast(self):
        request = urllib2.urlopen(self.FORECAST_URL + self.ip).read()

        wjson = json.loads(request)
        obs = wjson['forecast']
        return obs

    def current(self):
        if self.f_or_c == 'both':
            temp = self.conditions_data['temperature_string']
        elif self.f_or_c == 'F':
            temp = self.conditions_data['temp_f']
        else:
            temp = self.conditions_data['temp_c']
        text = shorten_text(self.conditions_data['weather'])
        icon_name = self.conditions_data['icon']
        self.set_icon(icon_name)

        print "%s, %s" % (text, temp)

    def current_forecast(self):
        today_forecast = self.forecast_data['simpleforecast']['forecastday'][0]
        print today_forecast['conditions']

    def forecast(self):
        forecast_list = self.forecast_data['simpleforecast']['forecastday'][1:]
        forecast_strings = []
        for forecast_day in forecast_list:
            high = forecast_day['high']['fahrenheit']
            low = forecast_day['low']['fahrenheit']
            conditions = forecast_day['conditions']
            weekday = forecast_day['date']['weekday_short']

            forecast_strings.append(
                "%s %s/%s %s" % (
                    weekday,
                    high,
                    low,
                    conditions
                )
            )
        print " | ".join(forecast_strings)

    def location(self):
        # print self.conditions_data['display_location']['city']
        print self.conditions_data['display_location']['full']

    def set_icon(self, imgname):
        current_icon = os.path.join(BASE_DIR, 'images', 'weathericon.png')
        new_icon = os.path.join(BASE_DIR, 'images', "%s.png" % imgname)
        print current_icon
        print new_icon
        if os.path.exists(current_icon):
            os.remove(current_icon)
        copy(new_icon, current_icon)

if __name__ == '__main__':
    w = Weather()
    w.run_tasks()