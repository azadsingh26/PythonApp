import datetime
from datetime import datetime, timedelta
from flask import Flask
import requests
import logging
import json
import os
import sys

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s DemoApp  : %(message)s')

app = Flask(__name__)

config_location=os.getcwd().split('/src')[0]+"/config/"
config_file_name="appConfiguration.json"

@app.route('/')
def get_rainfall_data():

    '''Main Entry Point For Get API Call  for Rain'''

    configurations=read_configs()
    print(configurations)
    try:
        api_url=configurations["apiUrl"]
        locations=configurations["location"]

        api_data=getDataFromApiURL(api_url)
        output=""
        
        for location in locations:
            response_from_findlocation=findLocationData(location,api_data)
            output=output+ "" + response_from_findlocation
        return output
    except:
        app.logger.error('Malformed Data. Please Check')
        print("Oops!", sys.exc_info()[0], "occurred.")
        return 'Malformed Data. Please Check'


def read_configs():
    ''' This functions read / loads configuration from config location and throws ou error, if file is not present'''
    try:
        
        with open(config_location+config_file_name,'r') as f:
            data = json.load(f)
        return data
    except:
        app.logger.error("File " +config_location+config_file_name + 'Not Present in Right Directory. Please check')
        print("File " +config_location+config_file_name + 'Not Present in Right Directory. Please check')
        print("Oops!", sys.exc_info()[0], "occurred.")


def getDataFromApiURL(api_url):

    ''' This function pulls the data from configured apiUrl and returns the response in json format. This also checks for api response'''
    r = requests.get(api_url)
    print(r.json())
    
    if (r.status_code!= 200):
        app.logger.error(api_url+ ": is down or incorrect. Please check")
        print(api_url+ ": is down or incorrect. Please check")
    else:    
        return r.json()

def findLocationData(location,api_data):


    for station in api_data["metadata"]["stations"]:
        if station["name"]==location:
            station_id=station["id"]
            response=raindataInformation(api_data,station_id)
            return location+","+response
    return "Not a Valid Location:" + location


def raindataInformation(api_data,id):

    for readings in api_data["items"]:
        now = datetime.now()

        current_time = now.strftime("%H:%M")
        print("Current Time =", current_time)
        



        for items in readings["readings"]:
            if id==items["station_id"]:
                rainfall=str(items["value"])            
                if items["value"]>0:
                    
                    return  str(current_time)  + ","+rainfall +"mm,Raining "
               
                return  str(current_time)  + ","+rainfall +"mm,Not Raining "

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=True)
    app.logger.info('Rainfall Service started')
    app.logger.warning('Warning level log')
