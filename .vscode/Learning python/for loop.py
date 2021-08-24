seats=["elias"]
x=input("enter name: ")
seats+=[x]
if not "elias" in seats:
    seats+=["elias"]
else:
    seats+=["chief","paul"]

for x in seats:
    print("hey " + x)

# counting letters
name="sudi abdalla"
count = 0
for i in name:
    count += 1

print(count)