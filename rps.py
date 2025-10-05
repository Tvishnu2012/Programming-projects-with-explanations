import random

print("Welcome to Rock, Paper, Scissors\n")

score = 0
cpuScore = 0
rps = ['rock', 'paper', 'scissors']

for _ in range(5):
    p1 = input("Rock, Paper or Scissors? ").lower()
    print("You: ", p1)
    cpu = random.choice(rps)
    print("The CPU chose: ", cpu)
    if cpu == 'rock' and p1 == 'rock':
        score * 1
        cpuScore * 1
    elif cpu == 'paper' and p1 == 'paper':
        score * 1
        cpuScore * 1
    elif cpu == 'scissors' and p1 == 'scissors':
        score * 1
        cpuScore * 1
    elif cpu == 'rock' and p1 == 'paper':
        score += 1
    elif cpu == 'rock' and p1 == 'scissors':
        cpuScore += 1
    elif cpu == 'paper' and p1 == 'rock':
        cpuScore += 1
    elif cpu == 'paper' and p1 == 'scissors':
        score += 1
    elif cpu == 'scissors' and p1 == 'rock':
        score += 1
    elif cpu == 'scissors' and p1 == 'paper':
        cpuScore += 1

print("Cpu's Score: ", cpuScore)
print("Your Score: ", score)
print()

if score == cpuScore:
    print("It is a tie!")
elif score > cpuScore:
    print("You won !!!")
elif score < cpuScore :
    print("The Cpu won. You lost :( ")