# Bytt ut til emoji

def main():
    bruker_tekst = str(input(">"))
    konvertert = convert(bruker_tekst)
    print(konvertert)

def convert(tekst):
    tekst = tekst.replace(":)", "🙂").replace(":(", "🙁")
    return tekst
    

main()