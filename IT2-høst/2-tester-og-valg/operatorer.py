# Aritmetriske operatorer - "matteoperatorer"

# +     # pluss
# -     # minus
# /     # dele
# *     # gange
# **    # opphøyd i, eks: 2**4 = 2*2*2*2
# %     # modolo -> finner resten eks: 5 % 2 -->> 1, du har 1 i rest


# if sekunder % 60 == 0:  # For hvert 60 sekund skjer det noe!


# Sammenligningsoperatorer

# >     Større enn
# >=    Større eller lik
# <     Mindre enn
# <=    Mindre eller lik
# ==    Lik
# !=    Ikke lik

print(3 > 2) # True
print(3 > 4) # False

logget_inn = False
alder = int(input("Hvor gammel er du? "))
myndig = alder >= 18
print(myndig) #True eller False, avhengig av alder som bruker skrev inn


# Logiske operatorer

# and   begge sider av and må være True for at hele skal bli True
# or    én av sidene trenger være True for at hele skal bli True
# not   snur verdien til en True eller False

alder = int(input("Hvor gammel er du?"))
arbeidsalder = alder > 16 and alder < 70

ikke_arbeidsdyktig = alder < 16 or alder > 70

not arbeidsalder # Hvis den var True, så blir den False.
