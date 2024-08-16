
def palindrome(num):
    result = str(num)[::-1]
    return result


    



number = 434

result = palindrome(number)

print(f"number is {number}")
print(f"number reversed is {result}")


if (number == result):
    print(f"{number} is a palindrome")


else:
    print(f"{number} is not a palindrome")