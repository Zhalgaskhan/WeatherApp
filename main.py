from flask import Flask, render_template
import requests
import datetime


app = Flask(__name__)
api_call = "https://api.openweathermap.org/data/2.5/weather?lat=55.7522&lon=37.6156&appid=754bc9a6066d458231b0d18a3aa5aa34&units=standard&lang=ru"
jsn = requests.get(api_call)
res = jsn.json()

def Kelvin_to_Celcius(k):
	return int(k-273)
	

weather_info = res['weather'][0]
time = datetime.datetime.now()
city = "Moscow"
country = res['sys']['country']
icon  = weather_info['icon']
main = weather_info['main']
description = weather_info['description']
temp = Kelvin_to_Celcius(res['main']['temp'])

out_res = [city, country, str(temp), main, description, str(time)]

enter_params = ''
for elem in out_res:
    enter_params += elem+' '



@app.route("/")
def hello_world(name=enter_params):
	return render_template('hello.html',name = name)


