import random
print("Wilkommen zum Mathe Quiz")

score = 0
for _ in range(10):
    x = random.randint(1, 1001)
    y = random.randint(1, 1001)

    print("What is", x, "-", y )
    antwort = input("What is your awnser? ")
    if int(antwort) == x - y :
        print("Richtig!!!")
        score += 1
    else:
        print("Oops es ist leider falsch:(")
        print("Die richtige Antwort ist", x - y)

print("Dein Punktzahl ist ", score)