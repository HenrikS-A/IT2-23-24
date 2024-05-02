liste = [6, -4, 7, -2, 8, -3, 9, -11]

minsteverdi = 0
for tall in liste:
    if tall < minsteverdi:
        minsteverdi = tall
print(minsteverdi)

maksverdi = 0
for tall in liste:
    if tall > maksverdi:
        maksverdi = tall
print(maksverdi)