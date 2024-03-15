import requests
from bs4 import BeautifulSoup

def hent_plasseringer() -> list[str, int]:
    """
    Scraper formel 1 sin nettside og henter plassering til førerne 
    og hvor mange poeng de har i fører-mesterskapet (denne blir ikke oppdatert direkte)
    """

    url = "https://www.formula1.com/en/results.html/2024/drivers.html"
    respons = requests.get(url, timeout=10)

    gammel_forer_plassering = {}
    innhold = BeautifulSoup(respons.content, "html.parser")
    for rad in innhold.select("tbody tr"):
        navn = rad.find("td", class_="").find("a").find("span", class_="hide-for-mobile").get_text()
        poeng = rad.find("td", class_="dark bold").get_text()
        gammel_forer_plassering[navn] = int(poeng)
    
    return gammel_forer_plassering

def hent_forertall(etternavn: str):
    url = f"https://api.openf1.org/v1/drivers?last_name={etternavn}"
    respons = requests.get(url, timeout=10)
    data = respons.json()
    forer_tall = data[0]["driver_number"]
    return forer_tall

def hent_forernavn(forertall: str):
    url = f"https://api.openf1.org/v1/drivers?driver_number={forertall}"
    respons = requests.get(url, timeout=10)
    data = respons.json()
    forer_navn = data[0]["last_name"]
    return forer_navn
     
def hent_naaverende_pos(forertall: int):
    url = f"https://api.openf1.org/v1/position?meeting_key=latest&session_key=latest&driver_number={forertall}"
    respons = requests.get(url, timeout=10)
    data = respons.json()
    if len(data) > 0:
        return data[-1]["position"]
    return 20

def hent_raskeste_runde():
    url = f"https://api.openf1.org/v1/laps?meeting_key=latest&session_key=latest"
    respons = requests.get(url, timeout=10)
    data = respons.json()
    
    runder = []
    for runde in data:
        if runde["is_pit_out_lap"] or runde["lap_duration"] is None:
            continue
        runder.append({"forer": runde["driver_number"], "rundetid": runde["lap_duration"]})
    
    runder_sortert = sorted(runder, key=lambda runde: runde["rundetid"])

    return runder_sortert[0]["forer"]
