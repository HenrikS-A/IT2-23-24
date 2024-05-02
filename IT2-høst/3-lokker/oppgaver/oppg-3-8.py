import re

tekst = """
«A Monster Calls»:
Et indre monster A Monster Calls (2011) er en tungt prisbelønnet britisk barnebok, skrevet av Patrick Ness, etter en idé av Siobhan Dowd som døde av kreft før hun selv rakk å skrive historien.
Jeg kjenner ikke til boken, men merket at den spesielle tilblivelseshistorien ga en viss tyngde til filmen til og med før jeg så den.
Man møter gjerne filmer som dette med et eget sett med forventninger, ofte preget av ærbødighet og respekt, på samme måte som man forholder seg litt annerledes til alvorlig syke mennesker enn man gjør til friske.
Alvorlig syke har kontakt med noe de ikke kan flykte fra, de er merket og de minner oss som foreløpig er friske om at livet er skjørt, kort og brutalt.
Som manusforfatter skjønner man raskt at sykdom står i en særstilling som drivkraft på film.
Sykdommer er nyttige fordi de bringer med seg en nødvendighet og et sett med spilleregler som umiddelbart er synlige for hvem som helst, men de er også farlige som fortellermessig størrelse, fordi de kan enda opp med å bli en mekanisme mer enn noe annet.
Rørende idé A Monster Calls går rett i strupen på hvordan en terminal kreftdiagnose hos en mor påvirker barnet.
Lewis MacDougall er nennsomt castet som 12-åringen Conor.
Han har et skjørt utseende og en tilbakeholdt spillemåte som er sjelden blant barneskuespillere.
Felicity Jones er like god som den døende moren.
Sigourney Weaver spiller bestemoren, men har ikke her samme naturlige tilstedeværelse som hun har på sitt beste.
Conor reagerer på den overhengende tragedien med å skape et indre monster.
Ideen er god og rørende, men den behandles litt stivt og spenningsfilms-aktig og vi må derfor helt til slutten av de to timene filmen varer for å komme inn i den følelsesmessige bevegelsen som burde ha ligget under fra første stund.
Jeg ser ikke bort ifra at grepet fungerer bedre i boken enn det gjør her.
Visuell fest Monsteret er en barlind som kommer til liv, med lysende øyne og Liam Neesons dype stemme.
Den er i slekt med entene, de levende trærne, i Ringenes Herre – To Tårn (2002), men også med flere av Transformers-skapningene.
Barlind-monsteret bringer Conor i kontakt med følelsene sine, men hindrer samtidig det emosjonelle planet i å virke i forgrunnen.
En åpenbar film å sammenligne med er Lasse Hallströms Mitt liv som hund (1985), som også handlet om en dødssyk mor, men var emosjonell, varm og overveldende fra første sekund.
Vi kommer veldig mye tettere på Ingemar Johansson enn vi gjør på Conor O´Malley.
Til gjengjeld er A Monster Calls, en visuell fest, med mørke, gotiskinspirerte scenarier, fine animerte sekvenser og i det hele tatt litt av en lekkerbisken – som ville vært ganske fantastisk hvis den hadde vært emosjonelt like solid som den er stilsikker.
"""


antall_mellomrom = 0
antall_linjer = 0
antall_spesielle_tegn = 0

for i in range(len(tekst)):
    if tekst[i] == " ":
        antall_mellomrom += 1

    if tekst[i] == "\n":
        antall_linjer += 1
    
    if tekst[i] in ["«", "»", ",", ".", "!", "-", ":", "´", "(", ")"]:
        antall_spesielle_tegn += 1

print(antall_mellomrom)
print(antall_linjer)
print(antall_spesielle_tegn)



# Finner antall ord som slutter på "er":

ren_tekst = re.sub(r"[«»,.!-:´()–]", "", tekst)     # Det her er regex - derfor bruker jeg r-string - "raw string lateral"
ren_tekst = ren_tekst.replace("\n", " ")

tekst_ordene = ren_tekst.split(" ")
slutter_paa_er = 0

for ord in tekst_ordene:
    if len(ord) == 0:
        continue
    else:
        if ord.endswith("er"):
            slutter_paa_er += 1

print(slutter_paa_er)



# Finner årstall

tekst_tall = re.findall(r"\d+", tekst) # Denne henter ut alle tall (digits), og står tallene samme, blir de slått sammen til én strenge med hele tallet.
antall_aarstall = 0

for tall in tekst_tall:
    if len(tall) == 4:          # Jeg antar at årstallene som blir nevnt i teksten har 4 sifte.
        antall_aarstall += 1

print(antall_aarstall)

# eller!!!!!
tekst_tall = re.findall(r"\d{4}", tekst) # Denne henter ut alle tall (digits) som har lengde på 4
antall_aarstall = len(tekst_tall)
print(antall_aarstall)

