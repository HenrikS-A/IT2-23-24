import requests
from flask import Flask

app = Flask(__name__)

def vaer(sted):
    url = f"https://wttr.in/{sted}?format=j1"
    respons = requests.get(url)
    data = respons.json()

    foles_som = data["current_condition"][0]["FeelsLikeC"]
    vaertype = data["current_condition"][0]["weatherDesc"][0]["value"]
    temp = data["current_condition"][0]["temp_C"]

    return vaertype, temp


@app.get("/")
def hjem():
    return "Du må skrive et sted i adressefeltet. For eksempel: http://127.0.0.1:5000/Sandvika"

@app.get("/<string:sted>")
def rute_sted(sted: str):
    vaertype, temperatur = vaer(sted)
    return f"Været i {sted} er {vaertype} og {temperatur} grader"

app.run(debug=True)
