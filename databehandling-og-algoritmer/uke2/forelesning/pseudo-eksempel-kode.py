
land = input("Hvilket land kommer du fra?\n> ").lower()

if land == "norge":
    print("$0.44 pr. sang")
elif land == "sverige":
    print("$0.34 pr. sang")
else:
    print("$0.22 pr. sang")


antall_streams = int(input("Hvor mange streams har du?\n> "))

if antall_streams > 30_000_000:
    print("Penger tjent pr. sang: 70%")
elif antall_streams > 1_400_000:
    print("Penger tjent pr. sang: 40%")
else:
    print("Penger tjent pr. sang: 0%")
