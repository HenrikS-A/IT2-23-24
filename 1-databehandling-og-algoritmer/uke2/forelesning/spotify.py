# Sandvikas Spotify bibliotek
# Versjon: 0.0.1
# Forfatter: thorcc
import requests
import json 

"""
Eksempel på bruk:
from spotify import weekly_top_songs_global

sanger = weekly_top_songs_global() 
"""

def weekly_top_songs_global():
    """Henter sangene i spillelisten "Weekly Top Songs: Global

    Returnerer
    ----------
    list<dict>
        En liste med ordbøker, der hver ordbok er en sang
        Eks på sang:
            {
                "navn": "Dead of Night", 
                "artist": "Orville Peck", 
                "bilde_url": "https://i.scdn.co/image/ab6761610000e5eb7b1eab5bbcfd5b2dd57c1753"
            }
    """


    spotify_url = "https://charts-spotify-com-service.spotify.com/public/v0/charts"
    respons = requests.get(spotify_url) # gjør en spørring til spotify_url (henter innholdet på nettadressen)
    data = json.loads(respons.content) # gjør innholdet om til en ordbok
    
    sanger = [] # En tom liste som skal fylles med sanger
    toppliste = data["chartEntryViewResponses"][0] # Henter ut den første listen, som er "Weekly Top Songs: Global"
    sangliste = toppliste["entries"]  # Henter listen med sanger
    for sang in sangliste: # Går gjennom hver sang i listen sangliste:
        # oppretter en ny ordbok for hver sang
        ny_sang = {
            "navn": sang["trackMetadata"]["trackName"],
            "artist": sang["trackMetadata"]["artists"][0]["name"],
            "bilde_url": sang["trackMetadata"]["displayImageUri"],
        }
        sanger.append(ny_sang) # legger ordboken ny_sang i listen sanger
    return sanger # returnerer listen sanger



sanger = weekly_top_songs_global()
fil = open("sanger.json", "w")
json.dump(sanger, fil, indent=2)
fil.close()

