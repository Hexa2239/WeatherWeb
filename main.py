import json
import os
import requests
from flask import Flask, request, send_file, jsonify

app = Flask("WeatherWeb")

@app.get("/")
def index():
    return send_file("./public/index.html"), 200

@app.get("/api/weather")
def getWeather():
    with open("./config.json", "r") as data:
        solid = data.read()
        jsonData = json.loads(solid)
    
    if (jsonData["weather_api_key"] != None):
        requestData = requests.get("http://api.weatherapi.com/v1/current.json?key=" + str(jsonData["weather_api_key"]) + "&q=" + str(request.args.get("area")) + "&aqi=no")
        
        return requestData.text
    else:
        return "No Weather API found", 200


app.run(port=44020, host="0.0.0.0")