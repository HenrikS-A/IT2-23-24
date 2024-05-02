telefonkatalog = {
    "Arne": 22334455,
    "Lisa": 95959595,
    "Jonas": 97959795,
    "Peder": 12345678
}

navn = input("Skriv inn et navn: ")

if navn in telefonkatalog.keys():
    print(telefonkatalog[navn])
else: 
    print("Navnet er ikke i telefonkatalogen.")
