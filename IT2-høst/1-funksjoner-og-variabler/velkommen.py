def main():
    person1 = spør_om_navn()
    si_velkommen(person1)


def spør_om_navn():
    navn = str(input("Hva heter du? \n\t--> "))
    navn = navn.title()

    return navn

def si_velkommen(person):
    fornavn, etternavn = person.split(" ")
    print(f"Velkommen til dette fantastiske programmeringsuniverset, {fornavn}!")


main()