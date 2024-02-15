
## Penger tjent per sang

### Pseudokode - naturlig språk:
```pseudo
Hent inn land fra bruker (input)
Hvis land er lik Norge:
    Print $0.44 per sang
Ellers hvis land er lik Sverige:
    Print $0.34 per sang
Ellers:
    Print $0.22 per sang
```

### Pseudokode - Udirs standard:
```pseudo
SET land TO READ "Hvilket land er du fra?"
IF land EQUAL TO "Norge"
    THEN DISPLAY "$0.44 per sang"
ELSE IF land EQUAL TO "Sverige"
    THEN DISPALY "0.34 per sang"
ELSE
    THEN DISPLAY "$0.22 per sang"
ENDIF
```

### Python kode:
```python
land = input("Hvilket land kommer du fra?\n> ").lower()
if land == "norge":
    print("$0.44 pr. sang")
elif land == "sverige":
    print("$0.34 pr. sang")
else:
    print("$0.22 pr. sang")
```

## Andel penger tjent per sang

### Pseudokode - naturlig språk:
```pseudo
Hent inn antall streams fra bruker
Hvis antall streams er større enn 30 000 000
    Print "penger tjent per sang lik 70%"
Ellers hvis antall streams er større enn 1 400 000
    Print "penger tjent per sang lik 40%"
Ellers 
    Print "penger tjent per sang lik 0%"
```

### Pseudokode - Udirs standard:
```pseudo
SET antall_streams TO READ "Hvor mange streams har du?"
IF antall_streams GREATER THAN 30 000 000
    THEN DISPLAY "penger tjent per sang: 70%"
ELSE IF antall_streams GREATER THAN 1 400 000
    THEN DISPLAY "penger tjent per sang: 40%"
ELSE
    THEN DISPLAY "penger tjent per sang: 0%"
ENDIF
```

### Python kode:
```python
antall_streams = int(input("Hvor mange streams har du?\n> "))
if antall_streams > 30_000_000:
    print("Penger tjent pr. sang: 70%")
elif antall_streams > 1_400_000:
    print("Penger tjent pr. sang: 40%")
else:
    print("Penger tjent pr. sang: 0%")
```
