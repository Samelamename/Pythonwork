age = int(input("Please enter age: "))
if age >= 18:
    print("You are in Cat A")
elif age == 16:
    print("You are in Cat B")
elif age < 16:
    print("You are in Cat C")
else:
    print("You do not have a Cat :(")
