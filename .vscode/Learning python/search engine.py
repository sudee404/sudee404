
def search(x,y):
    if y in x:
        return("Word found")
    else:
        return("Word not found")
    
text = input()
word = input()


print(search(text, word))