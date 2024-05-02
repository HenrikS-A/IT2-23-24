fargekode = str(input("Skriv inn en RGB-kode. (eks: 255 255 255): "))

r, g, b = fargekode.split(" ")

if r.isnumeric() and g.isnumeric() and b.isnumeric():
    r = int(r)
    g = int(g)
    b = int(b)


    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        print("Du har skrevet inn en korrekt fargekode!")
    else:
        print("Nei, nei, nei. En RGB-kode har bare tall mellom 0 og 255.")

else:
    print("Du kan bare skrive inn tall og mellomrom i fargekoden.")



