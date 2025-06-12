import requests


url = "https://api.openweathermap.org/data/2.5/weather"

params={
    "q":input("Enter city name: "),
    "appid":"cf34fa494594949dbbe8ca24c6117573",
    "units":"metric"
}
response =requests.get(url,params=params)
data=response.json()
if response.status_code == 200:

   print("City",data["name"])
   print("Description",data["weather"][0]['description'])
   print("Temp",data["main"]["temp"],"C")
   print("Status Code",response.status_code)
else:
   print("Error",response.status_code)