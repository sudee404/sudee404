you = your_attendance_to_school_this_year 
while True :
    print(you) 
if you == absent * 1: 
    print("first warning") 
    continue 
elif you == absent * 2: 
    print("second warning") 
    continue 
elif you == absent * 3: 
    print("last warning") 
    continue 
elif you == absent * 4: 
    print("you are out of school")