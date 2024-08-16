# Exercise Four

def remove_string(word, num):
    if num <= len(word):
           remove = word[num:]
           return remove
    else:
          print("Number is too long")
 

 




word = input("Enter a word:")
num = int(input("Enter a num: "))
result = remove_string(word, num)

print(f"Result is: {result}")