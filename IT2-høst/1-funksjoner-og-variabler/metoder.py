# Først litt om strings

navn = "Henrik" #doble
laerer = 'Thor' # eller enkle
favorittmat = ["Taco", "Pizza", "Tikka Masala", "Biff", "Pasta Carbonara"]

# EKSPERT:

# 3 anførselstegn, strings over flere linjer
f1_forere = """
Charles Leclerc
Carlos Sainz
Sebastian Vettel
Michael Schumacker
Kevin Magnussen
Fernando Alonso
Nikita MazeSPIN
"""

ironi = 'Dette var jo "kult"'  # Doble anførselstegn kan skrives inne i enkle

ironi = "Andreas' vits var \"kul\"" # Både doble og enkle, da må vi bruke bakoverstrek før tegnet
melding = "Hei!\n Så fint å se deg!" # \n = ny linje

print(ironi)


# --- String metoder ---

# Metoder er funksjoner som hører til objekter, en string er et eksempel på et objekt. 
# Vi har for eksempel .lower() og .upper() som gjør strings om til små og store bokstaver

navn = "Henrik Strøm-Andersen"
små = navn.lower()
print(små)

store = navn.upper()
print(store)