from flask import Flask
import requests
import datetime


app = Flask(__name__)
api_call = "https://api.openweathermap.org/data/2.5/weather?lat=55.7522&lon=37.6156&appid=754bc9a6066d458231b0d18a3aa5aa34&units=standard"
jsn = requests.get(api_call)
res = jsn.json()

def Kelvin_to_Celcius(k):
	return k-273
	

weather_info = res['weather'][0]
time = datetime.datetime.now()
city = "Moscow"
country = res['sys']['country']
icon  = weather_info['icon']
main = weather_info['main']
description = weather_info['description']
temp = res['main']['temp']

out_res = {}
out_res['icon']=icon
out_res['main']=main
out_res['description']=description
out_res['time']=time
out_res['city']=city
out_res['temp']=Kelvin_to_Celcius(int(temp))
out_res['country']=country

@app.route("/")
def hello_world():
	return out_res


