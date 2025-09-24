import random #imports the random module
print("Welcome to the Maths Quiz") #prints Welcome to the Maths Quiz

score = 0 #makes a variable called score with the value 0
highscore = 0 #makes a variable called highscore with the value 0
numberOfQuestions = 10 #creates a variable called numberOfQuestions assigning the value 10 to it

for _ in range(numberOfQuestions): #makes a loop that has the variable _ so taht it keeps counting till 10 from the 
    #numberOfQuestions varible.So it repeats the code under this that has a tab space to the side numberOfQuestions times.
    x = random.randint(1, 101) #makes a variable called x with a random value from 0-100 uning the random module from which 0 
    #is the first number.
    y = random.randint(1, 11) #makes a variable called y with a random value from 0-10 uning the random module from which 0 
    #is the first number.
 
    print("What is", x, "divided by", y ) #prints 'What is' and then the value of x that is random 'divided by' the value of y 
    #which is also random 
    answer = input("What is your answer? ") #makes a variable called answer with the value that the user gives and prints 
    #What is your answer?
    if float(answer) == x / y : #this is an if clause where it checks if the answer of the user which will then be formated 
        #as float is the quotient of the values of x and y if yes it
        print("Correct!!!") #prints Correct!!!
        score += 1 #and adds 1 to the score variable
    else: #but if the users answer is wrong it prints
        print("Oops it was wrong :( ") #Oops it was wrong :( 
        print("The correct answer is ", x / y) #and then gives the correct answer by dividing x by y.

print("You scored", score) #here it prints 'You scored: ' and then it prints the score variable which will 
#have changed to something more than 0 if the user gave any correct answers in the 10 Questions

if score > highscore: #here it checks if the score is bigger than the highscore
    highscore = score #if score is bigger than highscore then highscore will have the new value of score 
    print("Your highscore is currently: ", highscore) #here it prints 'Your highscore is currently: ' and then the
    #value of highscore
else: #else it will
    print("Dein Highscore ist ", highscore) #print 'You highscore is still: ' then the value of the variable highscore