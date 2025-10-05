import random #imports the random module

print("Welcome to Rock, Paper, Scissors\n") #prints 'Welcome to Rock, Paper, Scissors' the \n makes a newline though another print()
#without arguments will be enough as well.

score = 0 #makes a variable called score with the value 0
cpuScore = 0 #makes a variable called cpuScore with the value 0
rps = ['rock', 'paper', 'scissors'] #makes a list called rps with the content 'rock', 'paper' and 'scissors

for _ in range(5): #a for loop to repeat the code in it 5 times
    p1 = input("Rock, Paper or Scissors? ").lower() #makes a user input called p1.teh .lower() makes the computer get the awnser in
    #lowercase so that even if the user gives everything in case letters that the computer does not see it as a mistake.
    print("You: ", p1) #this prints "You: "and then your input here it will be clear that the .lower() works as it is always in 
    #lowercase
    cpu = random.choice(rps) #makes a variable called cpu and the random.choice(rps) takes a random word from the rps list
    print("The CPU chose: ", cpu) #here it prints the random word that has been selected using th erandom.choice()
    if cpu == 'rock' and p1 == 'rock': #here it gives the computer the senarios in which it shall change the score
        score * 1 #this is optional as well as teh otehr ones in the senarios because it multiplies the score with one leaving
        #it just as it was
        cpuScore * 1 #this one as well
    elif cpu == 'paper' and p1 == 'paper': #here we use elif which is else if
        score * 1 #this and the other one is not necessary
        cpuScore * 1
    elif cpu == 'scissors' and p1 == 'scissors':
        score * 1
        cpuScore * 1
    elif cpu == 'rock' and p1 == 'paper':
        score += 1 #here the computer add 1 to the current value of score
    elif cpu == 'rock' and p1 == 'scissors':
        cpuScore += 1 #here the same as above happens with the cpuScore variable. So only the varaiable changed and the rest is still
        #same.
    elif cpu == 'paper' and p1 == 'rock':
        cpuScore += 1
    elif cpu == 'paper' and p1 == 'scissors':
        score += 1
    elif cpu == 'scissors' and p1 == 'rock':
        score += 1
    elif cpu == 'scissors' and p1 == 'paper':
        cpuScore += 1

print("Cpu's Score: ", cpuScore) #here it prints the value of the cpuScore variable after the loop is over so this is the score of 
#the cpu after the whole game
print("Your Score: ", score, "\n") #here the same and the \n makes a newline

if score == cpuScore: #here the computer checks the score to tell who won. Here it checks if the score of teh user is teh same as 
    #the score of the computer
    print("It is a tie!") #it it is then it prints "It is a tie!"
elif score > cpuScore: #here it checks weather the score of the user is bigge than the one of the computer
    print("You won !!!") #if it is then i t prints "You won !!!"
else: #everything else is in this else case.
    print("The Cpu won. You lost :( ") #here it prints "The Cpu won. You lost :(".