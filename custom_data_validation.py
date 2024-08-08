

username = input("Enter username: ")

if 5 <= len(username) <= 15:
    try:
        age = int(input("Enter age: "))
        if age >= 18 and age <= 100:
            email = input("Enter email ")
            if "@" in email:
                    print("You are eligible for validation")
            else: 
                 print("Your email requires an @")
        else:
            print("Age must be between 18 and 100")
    except ValueError:
        print("Enter a number")


else:
    print("Username must be between 5 and 15 characters long")



