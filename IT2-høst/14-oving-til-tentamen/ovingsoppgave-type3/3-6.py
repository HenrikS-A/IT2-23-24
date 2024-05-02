
def legg_inn_null_maal(lagliste: list[str]):
    return {lag: 0 for lag in lagliste}

a = legg_inn_null_maal(["Brann", "Molde"])
print(a)
