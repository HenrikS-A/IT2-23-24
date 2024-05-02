
def vinnerlag(hjemmelag: str, bortelag: str, hjemmemaal: int, bortemaal: int):
    if hjemmemaal > bortemaal:
        return hjemmelag
    elif hjemmemaal == bortemaal:
        return "uavgjort"
    elif hjemmemaal < bortemaal:
        return bortelag
    else:
        print("Nå har noe feil skjedd...")

a = vinnerlag("Brann", "Molde", 2, 2)
print(a)
