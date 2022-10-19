import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess ")
count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))

    if x == guess:
        print("You Won!")
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")


#####OUTPUT######

Enter Lower bound:- 1
Enter Upper bound:- 9

	You've only  3  chances to guess 
Guess a number:- 5
You guessed too small!
Guess a number:- 9
You Guessed too high!
Guess a number:- 7
You Won!
Congratulations you did it in  3  try