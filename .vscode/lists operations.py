seats=["elias"]
x=input("enter name: ")
seats+=[x]
print("sudi" in seats)
if not "elias" in seats:
    seats+=["elias"]
else:
    seats+=["chief","paul"]
print("elias" in seats)
print("chief" in seats)
print("paul" in seats)