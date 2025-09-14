import random #imports the random module
print("Welcome to the Maths Quiz") #prints welcome

numberOfQuestions = 10

score = 0
for _ in range(numberOfQuestions):
    x = random.randint(1, 1001)
    y = random.randint(1, 1001)

    print("What is", x, "+", y )
    awnser = input("What is your awnser? ")
    if float(awnser) == x + y :
        print("Richtig!!!")
        score += 1
    else:
        print("Oops it was wrong :(")
        print("Die richtige Antwort ist", x + y)

print("Dein Punktzahl ist ", score)

prozent = (score/numberOfQuestions) * 100
print("Du hast ", prozent,"% der Fragen beantwortet") 