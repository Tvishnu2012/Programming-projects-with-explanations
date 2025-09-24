import random #here it is the same as in the mathsQuizDivide.py but with a '-' instead of a '/' so for subtraction
#,no highscore and with slighly different text that will be printed.
print("Wilkommen zum Mathe Quiz")

score = 0
for _ in range(10):
    x = random.randint(1, 1001)
    y = random.randint(1, 1001)

    print("What is", x, "-", y )
    antwort = input("What is your answer? ")
    if int(antwort) == x - y :
        print("Correct!!!")
        score += 1
    else:
        print("Oops that was wrong :(")
        print("The correct answer is: ", x - y)

print("You scored: ", score)