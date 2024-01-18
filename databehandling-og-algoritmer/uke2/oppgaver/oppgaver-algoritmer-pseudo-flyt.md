# Oppgaver - Algoritmer, pseudokode og flytdiagram

## Oppg. 1:
- Svar: C

## Oppg. 2:
- Svar: C

## Oppg. 3:
- Svar: C

## Oppg. 4:
- Svar: C

## Oppg. 5:
- Svar: D

## Oppg. 6:
- Svar: 1, 3

## Oppg. 7:
- Flytdiagrammet:

![flytdiagram](oppg-7-flytdiagram.png)

## Oppg. 8:
```pseudo

FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION

SET totalsum TO 0
SET i TO 0
FOR hver i LESSER THAN OR EQUAL TO 10
    CALL trekanttall (i) RETURNING nytt trekanttall
    INCREMENT totalsum BY nytt trekanttall
ENDFOR

DISPLAY totalsum

```

## Oppg. 9:
- Svar: 4

## Oppg. 10:
- Svar:
  F-1,
  H-2,
  A-3,
  B-4,
  C-5,
  G-6,
  E-7,
  D-8,

## Oppg. 11:
- A:
  - Svar: A, D
- B:
  - Svar: Svaralternativ D foretrekker jeg. Mye kortere og simplere algoritme, og den avslutter med en gang den finner det nest siste tallet uten å gå gjennom hele listen uten grunn.

## Oppg. 12:
- A:
  - Svar: 3
- B:
  - Svar: -






