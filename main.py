apikey = TOKEN_API

parameters = {
    "appid" : apikey,
    "lat" :"-20.336840",
    "lon" :"-40.291931",
    "cnt" : "20",
}
from twilio.rest import Client
import requests
account_sid = ACCOUNT
auth_token = TOKEN_AUTH

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()
will_rain = False
for hours in data["list"]:
    rain = hours["weather"][0]["id"]
    if rain <700 :
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring umbrella",
        from_="+19786985643",
        to="+5527996423551",
    )
    print(message.status)


# if id< 700 :bring umbrella
