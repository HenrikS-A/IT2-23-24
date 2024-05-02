import re

camel_case = input("camelCase: ")
camel_case_ord = re.split( "(?=[A-ZÆØÅ])", camel_case) # splitter på mellomrommet rett før stor bokstav

snake_case = "_".join(camel_case_ord).lower() # Setter sammen alle elementene fra listen over til én strenge med _ mellom elementene, og så gjør den alt til små bokstaver.
print(f"snake_case: {snake_case}")
