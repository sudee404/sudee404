#program takes user input
#generates a random number
#compares both numbers
#you win if similar within 3 tries
#you lose if all 3 tries are wrong


import random

user=int(input("Guess number: "))
rand=random.choice(range(1,11))
tips=["less than 5","greater than 5","odd number","even number","divisible by 5","It is a prime number"]

if user==rand:
    print(f"Correct guess.\nThe number is {rand}")

elif user!=rand:
    print("Wrong Guess")
    #less than 5
    if user<5 and rand<5:
        print("Tip: " + tips[0])
        user=int(input("Guess Again: "))
        if user==rand:
            print(f"Correct guess.\nThe number is {rand}")
        elif rand%2==0:
            print("Wrong Guess")
            print("Tip: " + tips[5])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")
        else:
            print("Wrong Guess")
            print("Tip: " + tips[2])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")

    #less than 5
    elif user>=5 and rand<5:
        print("Tip: " + tips[0])
        user=int(input("Guess Again: "))
        if user==rand:
            print(f"Correct guess.\nThe number is {rand}")
        elif rand%2==0:
            print("Wrong Guess")
            print("Tip: " + tips[3])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")
        else:
            print("Wrong Guess")
            print("Tip: " + tips[2])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")


    #greater than 5
    elif user>5 and rand>5:
        print("Tip: " + tips[1])
        user=int(input("Guess Again: "))
        if user==rand:
            print(f"Correct guess.\nThe number is {rand}")
        elif rand%2==0:
            print("Wrong Guess")
            print("Tip: " + tips[5])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")
        else:
            print("Wrong Guess")
            print("Tip: " + tips[2])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")


    #greater than 5
    elif user<=5 and rand>5:
        print("Tip: " + tips[1])
        user=int(input("Guess Again: "))
        if user==rand:
            print(f"Correct guess.\nThe number is {rand}")
        elif rand%2==0:
            print("Wrong Guess")
            print("Tip: " + tips[3])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")
        else:
            print("Wrong Guess")
            print("Tip: " + tips[2])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")
    #5 and 10
    elif rand%5==0:
        print("Tip: " + tips[4])
        user=int(input("Guess Again: "))
        if user==rand:
            print(f"Correct guess.\nThe number is {rand}")
        elif rand%2==0:
            print("Wrong Guess")
            print("Tip: " + tips[3])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")
        else:
            print("Wrong Guess")
            print("Tip: " + tips[2])
            user=int(input("Guess Again: "))
            if user==rand:
                print(f"Correct guess.\nThe number is {rand}")
            else:
                    print("You lose")

else:
    print("Enter a number between 1 and 10")
           
