print("This is a python quiz")
score = 0

#Question 1
antwort1 = input("What is the capital of Germany? ").lower()
if antwort1 == "berlin":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 2
antwort2 = input("What is the capital of France? ").lower().strip()
if antwort2 == "paris":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 3
antwort3 = input("What is the capital of Norway? ").lower().strip()
if antwort3 == "oslo":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 4
antwort4 = input("What is the capital of Finnland? ").lower().strip()
if antwort4 == "helsinki":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 5
antwort5 = input("What is the capital of the USA? ").lower().strip()
if antwort5 == "washington dc":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")
#Question 6
antwort6 = input("What is the capital of Sweden? ").lower().strip()
if antwort6 == "stockholm":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 7
antwort7 = input("What is the capital of Russia? ").lower().strip()
if antwort7 == "moscow":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

print("Your score is", score)

percentage = (score/7) * 100
print("You scored ", percentage, "%")
