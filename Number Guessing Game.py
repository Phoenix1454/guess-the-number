"""You have to build a "Number Guessing Game," in which a winning number
 is set to some integer value. The Program should take input from the user, 
 and if the entered number is less than the winning number, 
 a message should display that the number is smaller and vice versa.
Instructions:

1. You are free to use anything we've studied till now.
2. The number of guesses should be limited, i.e (5 or 9).
3. Print the number of guesses left.
4. Print the number of guesses he took to win the game.
5. “Game Over” message should display if the number of guesses becomes equal to 0.
You are advised to participate in solving this problem. This task helps you to become 
a good problem solver and helps you accepting the challenge and acquiring new skills."""

n = 18
guesses = 9
g = 1
print("You have ", guesses, " guesses")
while(guesses>0):
    print("Enter your ",g," guess here", end="")
    q = int(input())
    if(q == n):
        print("Bravo you have gussed correct that is ",n,"in just ", g, "gusses")
        break
    elif(q != n):
        if(q>n):
            print("The number is smaller than your guess")
        else:
            print("The number is greater than your guess")
    g = g+1
    guesses = guesses - 1
    if(guesses == 0):
        print("You are out of gusses")
        print("Game over")
    else:
        continue    

