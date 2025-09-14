import random
print("Wilkommen zum Mathe Quiz")

score = 0
highscore = 0
for _ in range(10):
    x = random.randint(1, 101)
    y = random.randint(1, 11)

    print("What is", x, "geteilt durch", y )
    antwort = input("What is your awnser? ")
    if float(antwort) == x / y :
        print("Richtig!!!")
        score += 1
    else:
        print("Oops es ist leider falsch :( ")
        print("Die richtige Antwort ist", x / y)

print("Dein Punktzahl ist ", score)

if score > highscore:
    highscore = score
    print("Dein Highscore ist jetzt: ", highscore)
else:
    print("Dein Highscore ist ", highscore)