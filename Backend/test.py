year = int(input("Which year do you want to check:"))

if year % 100 == 0:
    if year % 400 == 0:
        print("schaltjahr")
    else:
        print("not schaltjahr")
elif year % 4 == 0:
    print("Schaltjahr")
else:
    print("not Schaltjahr")
