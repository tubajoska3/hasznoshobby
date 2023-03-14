import random
from pprint import pprint
#4. Feladat
# Készíts egy listát amely 8 diák adatait tartalmazza. A lista elemei szótárak legyenek, egy-egy szótár egy-egy diák adatait tárolja. A szótárban lévő kulcsok és a hozzájuk tartozó értékek:
# "név": a vezeteknevek és a keresztnevek nevű listából véletlenszerűen választott és párosított elemek
# "életkor": véletlenszám [14;19] intervallumban
# "évfolyam": véletlenszám [9;12] intervallumban
# "osztály": A, B, C vagy D lehet
# "cím": beágyazott szótár melynek kulcsai:
# "település": telepulesek nevű listából véletlenszerűen választva
# "utca": utcak nevű listából véletlenszerűen választva
# "házszám": véletlenszám [1;50] intervallumban
vezeteknevek = ["Kiss", "Horváth", "Szabó", "Pethő", "Szalai", "Nagy"]
keresztnevek = ["Petra", "Ádám", "Levente", "Zoé", "Hanna" ]
telepulesek = ["Sopron", "Fertőszentmiklós", "Harka", "Kópháza", "Fertőd", "Újkér" ]
utcak = ["Fő", "Kossuth", "Győri", "Petőfi", "Vadvirág", "Iskola"]
osztaly = ['A','B','C','D']
  
diak_adatok = [
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
    {
    'nev': random.choice(vezeteknevek) +' '+ random.choice(keresztnevek),
    'eletkor': random.randint(14,19),
    'evfolyam': random.randint(9,12),
    'osztaly': random.choice(osztaly),
    'cim': {
        'telepules': random.choice(telepulesek),
        'utca': random.choice(utcak),
        'hazszam': random.randint(1,50)
    },
    },
]
pprint(diak_adatok, sort_dicts=False)