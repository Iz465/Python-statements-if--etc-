

# Exercise One

def multiplication(num1,num2):
    calculation = num1 * num2

    if calculation <= 1000:
        return calculation
    
    else:
        return num1 + num2


result = multiplication(10,40)
print(result)

result = multiplication(50,60)
print(result)


# Exercise Two

print("\nExercise Two")
def adding(num1, num2):
    calculation = num1 + num2
    return calculation


for num in range(0,10):
    if num > 0:
        previous_num = num - 1
    else:
        previous_num = 0
    result = adding(num, previous_num)
    print(f"Current Number is: {num} Previous Number is: {previous_num} Sum is: {result}")


# Exercise Three

print("\nExercise Three")

word = input("Enter Word: ")

print("Original string", word)

size = len(word)

print("Printing only even index")

for i in range(0,size,2):
    print(f"Index {i}: {word[i]}")






