import random

def compare(c,u,r,p,s):
    while c==u:
            print("Draw. Try again")
            c=random.choice(picks)
            u=input("Pick again : ")
            continue

    while c!=u:
        if c==r and u==p:
            print("You win.Paper covers Rock")
            break
        elif c==p and u==s:
            print("You win.Scissor cuts Paper")
            break
        elif c==s and u==r:
            print("You win.Rock breaks Scissors")
            break
        else:
            if u==r and c==p:
                print("You lose.Paper covers Rock")
                break
            elif u==p and c==s:
                print("You lose.Scissor cuts Paper")
                break
            else:
                print("You lose.Rock breaks Scissors")
            break

picks=["rock","paper","scissors"]
user=input("Enter your pick: ")
comp=random.choice(picks)
compare(comp,user,picks[0],picks[1],picks[2])