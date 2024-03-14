import requests
from bs4 import BeautifulSoup

def hent_plasseringer() -> list[str, int]:
    """
    Scraper formel 1 sin nettside og henter plassering til førerne 
    og hvor mange poeng de har i fører-mesterskapet
    """

    url = "https://www.formula1.com/en/results.html/2024/drivers.html"
    respons = requests.get(url, timeout=10)

    innhold = BeautifulSoup(respons.content, "html.parser")

    gammel_forer_plassering = {}
    for rad in innhold.select("tbody tr"):
        navn = rad.find("td", class_="").find("a").find("span", class_="hide-for-mobile").get_text()
        poeng = rad.find("td", class_="dark bold").get_text()
        gammel_forer_plassering[navn] = int(poeng)

    return gammel_forer_plassering


def hent_forertall(etternavn: str):
    url = f"https://api.openf1.org/v1/drivers?meeting_key=latest&session_key=latest&last_name={etternavn}"
    respons = requests.get(url, timeout=10)
    data = respons.json()
    forer_tall = data[0]["driver_number"]
    return forer_tall


def hent_naaverende_pos(forertall: int):
    url = f"https://api.openf1.org/v1/position?meeting_key=latest&session_key=latest&driver_number={forertall}"
    respons = requests.get(url, timeout=10)
    data = respons.json()
    return data[-1]["position"]