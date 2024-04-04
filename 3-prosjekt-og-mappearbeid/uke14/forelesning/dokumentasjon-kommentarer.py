
# ¡Hola, amigo!

"""
Kommentar
som 
går
over
flere
linjer! 
WOW!!
"""

# En kommentar skal maks være 72 tegn i følge pythons stilguide (PEP)
# En linje i python skal ikke være lenger til høyre enn Col 72 (se nede)

# Hvis en kommentar må gå over to linjer, fordi den er lengre enn 
# 72 tegn, bruker vi som regel hashtags og ikke triple anførselstegn

# Triple anførselstegn bruker vi som regel
# i spesielle kommentarer, som f.eks. i docstrings



# -- Eksempel --
""" Dette er en dockstring, som gir en overordnet 
    forklaring av hva programmet gjør.
    De skrives med 3 anførselstegn.

Et program som kaster en terning

"""

import random

# Et tilfeldig tall fra og med 1 til og med 6
tilfeldig = random.randint(1, 6)
print(f"Du fikk {tilfeldig}")

# Kommenter det du ikke klarer (uten kommentar) å forklare selv
# eller det som ikke sier seg selv
# -- --



# Hovedsakelig er docstrings til de som leser/bruker programmet,
# mens kommentarene er mer for utviklerne som skal endre på programmet.

# Kommentarer er for utviklere, mens dokumentasjon er for brukere.

