import random

total_score = 0
user = []
comp = []
for i in range(10):
    n= int(input("Guess a number:"))
    nc = random.randint(1,100)
    user.append(n)
    comp.append(nc)
    print("Computer number was:" , nc)
    if n < nc :
        score = -1
    elif n == nc :
        score = 3
    elif n > nc :
        score = 1
    total_score += score
    print(f"score={score}")
print(f"YOUR TOTAL SCORE: {total_score}")
if total_score > 0:
    print("You win!")
if total_score < 0:
    print("Computer wins,Better luck next time!")
   
