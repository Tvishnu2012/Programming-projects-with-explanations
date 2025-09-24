print("This is a Geography quiz") #prints "This is a Geografy Quiz"
score = 0 #makes a variable called score with the value 0 

#Question 1 #this is a comment telling the question number this will not be displayed
answer1 = input("What is the capital of Germany? ").lower().strip() #makes a variable called answer1 that has 
#the user input as value. The .lower() makes the computer get the answer in lowercase no matter how the user enters it. The .strip()
#will make teh computer ignore any spaces in the start and end so the user can type a space in front of the answer he/she gives and 
#still get correct if the answer was spelled correctly and is correct.
if answer1 == "berlin": #this checks if the answer that the computer gets is berlin in this case and it is writen in lowercase because
# we used the .lower() in the input. If it is berlin then it
  print("Great job!!!") # prints 'Great job!!!'
  score += 1 # and adds 1 to the score variable
else: #else it 
  print("Oops that was wrong!") #prints 'Oops it was wrong!'

#Question 2 #same as for Question 1 but with different Question, answer and variable names
answer2 = input("What is the capital of France? ").lower().strip()
if answer2 == "paris":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 3 #same as for Question 1 but with different Question, answer and variable names
answer3 = input("What is the capital of Norway? ").lower().strip()
if answer3 == "oslo":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 4 #same as for Question 1 but with different Question, answer and variable names
answer4 = input("What is the capital of Finnland? ").lower().strip()
if answer4 == "helsinki":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 5 #same as for Question 1 but with different Question, answer and variable names
answer5 = input("What is the capital of the USA? ").lower().strip()
if answer5 == "washington dc":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 6 #same as for Question 1 but with different Question, answer and variable names
answer6 = input("What is the capital of Sweden? ").lower().strip()
if answer6 == "stockholm":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

#Question 7 #same as for Question 1 but with different Question, answer and variable names
answer7 = input("What is the capital of Russia? ").lower().strip()
if answer7 == "moscow":
  print("Great job!!!")
  score += 1
else:
  print("Oops that was wrong!")

print("Your score is", score) #here it prints teh final value of the score variable

percentage = (score/7) * 100 #here it makes a variable called percentage which has teh value of the
#variable score divided by the number of Question which shall be made more if you add more questions
print("You got ", percentage, "% correctly of the complete Quiz") #here it prints 'You got ' the value of percentage '% correctly of the complete Quiz '
