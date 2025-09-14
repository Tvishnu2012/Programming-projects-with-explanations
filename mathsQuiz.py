import random
print("Wilkommen zum Mathe Quiz")

anzahlFragen = 10

score = 0
for _ in range(anzahlFragen):
    x = random.randint(1, 1001)
    y = random.randint(1, 1001)

    print("What is", x, "+", y )
    antwort = input("What is your awnser? ")
    if float(antwort) == x + y :
        print("Richtig!!!")
        score += 1
    else:
        print("Oops es ist leider falsch:(")
        print("Die richtige Antwort ist", x + y)

print("Dein Punktzahl ist ", score)

prozent = (score/anzahlFragen) * 100
print("Du hast ", prozent,"% der Fragen beantwortet") 