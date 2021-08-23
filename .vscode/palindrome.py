#palindrome check
choice=input("enter n for number and w for a word: ")
if choice=="n":
    num=int(input("enter number: "))
    x=str(num)
    y=x[::-1]
    if int(y)==num:
        print("Is a palindrome")

    else:
        print("Is not a palindrome")

elif choice=="w":
    word = input("enter word:")
    y=word[::-1]
    if y==word:
        print("Is a palindrome")

    else:
        print("Is not a palindrome")

else:
    print("Wrong input")