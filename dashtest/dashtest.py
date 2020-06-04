import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import requests
import json
from pprint import pprint

city = input('City : ')

# get units to fahrenheit
url= 'https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02'.format(city)

#get url using requests
req = requests.get(url)

#format data in json
data = req.json()
temp = data['main']['temp']


app = dash.Dash(__name__)

app.layout = html.Div(
    html.H1(children="Michael Shannon Dashboard")
)

if __name__== "__main__":
    app.run_server(debug=True)