import random #imports the random module
print("Welcome to the Maths Quiz") #prints "Welcome to the Maths Quiz"

numberOfQuestions = 10 #creates a variable called numberOfQuestions assigning the value 10 to it

score = 0 #creates a variable called score and gives it the value 0
for _ in range(numberOfQuestions): # this makes a loop that repeats numberOfQuestions times.
    x = random.randint(1, 1001) # while the loop runs it will pick a random number from 0-1000 using the random module
    #1 meaning to start from 0 as python starts counting from 0 making it the first number till the 1001th number which is 1000
    y = random.randint(1, 1001) #same here

    print("What is", x, "+", y ) #then here it prints "What is" x + y but the x and y are outside of the double qoutes because
    #they are variabes that cannot be writen inside the double qoutes as it will print what is x + y but we want it to ask how much
    #the variable x which can be any number from 0-1000 + the variable y is both having a random value so you have it outside the "".
    awnser = input("What is your awnser? ") #this makes a variale called awnser with the value that is the awnser of the user
    if float(awnser) == x + y : #here it checks if the awnser of the user is correct if it is the correct awnser: 
        print("Correct!") #it prints Correct! then
        score += 1 #adds 1 to the current value of the variable score
    else: #else
        print("Oops it was wrong :(") #it prints Oops it was wrong and 
        print("The correct awnser is", x + y) #prints 'The correct awnser is' and then adds the variables x and y and prints the awnser with the text. 

print("Your score is ", score) # after the loop is over it prints 'Your score is' and then the score variable which will have changed
#because of the added score of the correct awnsers

percentage = (score/numberOfQuestions) * 100 #here it makes a variable called percentage that has the value of the score
#variable divided by numberOfQuestions multiplied by 100 which is the percentage
print("You awnsered ", percentage,"% of the Quiz correctly")  #here it prints 'you awnsered' the variable percentage that fluctuates accordingly to the correctly
#awnsered Questions etc... that are explained near the percentage variable.