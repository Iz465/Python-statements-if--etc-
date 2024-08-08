



while True: 
    score = int(input("Enter your score "))
    grade = ""

    if score >= 90:
        grade = "A"

    elif score >= 75:
        grade = "B"

    elif score >= 60:
        grade = "C"

    elif score >= 50:
        grade = "D"

    else:
        grade = "F"


    print(f"Your grade is {grade}\n")
    again = input("Again? Y/N: ")
    if again == "y":
        continue
    if again == "n":
        break




