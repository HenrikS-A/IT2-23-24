"""
Programmet finner arealet av en trekant
"""

grunnlinje = float(input("Grunnlinje (cm): "))
hoyde = float(input("Høyde (cm): "))
 
# Deler på 2 fordi jeg finner arealet av en trekant
areal = grunnlinje*hoyde/2
print(f"Arealet er {areal} cm^2")
