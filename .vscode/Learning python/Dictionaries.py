#dictionaries
ages={"sudi":21,"chief":20,"issa":22}
print(ages["chief"])
print(ages["sudi"])
print(ages["issa"])
print("chief" in ages)
print("sudi" in ages)
#only keys work and not values
print(21 in ages)

#dictionary functions
print(ages.get("chief"))
print(ages.get(20,"not found"))
print(len(ages))