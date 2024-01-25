import geocoder
import requests

def hente_vaerdata(x_koord, y_koord):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/complete"
    
    parametere = {
        "lat": x_koord,
        "lon": y_koord
    }
    headers = {
        "User-Agent": "Elev ved Sandvika VGS - henrikstro@viken.no"
    }
    respons = requests.get(url, parametere, headers=headers, timeout=10)
    data = respons.json()

    return data


sted = input("Skriv posisjonen:\n > ")
g = geocoder.arcgis(sted)
pos = g.json

x_koordinat, y_koordinat = pos["lat"], pos["lng"]
print(f"{pos['address']}: {x_koordinat}, {y_koordinat}")


vaerdata = hente_vaerdata(x_koordinat, y_koordinat)

temp = vaerdata["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
vaerbeskrivelse = vaerdata["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]

print(temp, "-", vaerbeskrivelse)
