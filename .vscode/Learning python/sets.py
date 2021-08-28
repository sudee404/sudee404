food={"banana","oranges","tomatoes","apples"}
vegies={"tomatoes","onions","kales"}
for s in vegies:
    if not s in food:
        print(s)

d=food-vegies
print(d)