import random

dice = input("Do you want to roll a dice?")
if dice == 'yes' or dice == 'Yes':
    yes = random.randint(1,6)
else:
    exit()
if yes == 1:
    print ("[-----]")
    print ("[     ]")
    print ("[  O  ]")
    print ("[     ]")
    print ("[-----]")
    exit()
elif yes == 2:
    print ("[-----]")
    print ("[O    ]")
    print ("[     ]")
    print ("[    O]")
    print ("[-----]")
    exit()
elif yes == 3:
    print ("[-----]")
    print ("[O    ]")
    print ("[  O  ]")
    print ("[    O]")
    print ("[-----]")
    exit()
elif yes == 4:
    print ("[-----]")
    print ("[O   O]")
    print ("[     ]")
    print ("[O   O]")
    print ("[-----]")
    exit()
elif yes == 5:
    print ("[-----]")
    print ("[O   O]")
    print ("[  O  ]")
    print ("[O   O]")
    print ("[-----]")
    exit()
elif yes == 6:
    print ("[-----]")
    print ("[O   O]")
    print ("[O   O]")
    print ("[O   O]")
    print ("[-----]")
    exit()
else:
    exit()
