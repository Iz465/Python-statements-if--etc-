

username = input("Enter username: ")

if len(username) >= 5 and len(username) <= 15:
    age = int(input("Enter age: "))
    if age >= 18 and age <= 100:
        email = input("Enter email")
        email_check = ["@"]
        for check in email_check:
            if check in email_check:
                "You are eligible for validation"
            else: "Your email requires an @"

    else:
        print("Age must be between 18 and 100")


else:
    print("Username must be between 5 and 15 characters long")



