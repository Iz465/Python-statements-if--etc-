def reverse_list(num_list):
  list_length = len(num_list)
  reversed_list = []
  for num in range(list_length):
    reversed_list.append(num_list[-1])
    num_list.pop()
  return reversed_list  

num_list = [1,4,6,7,1,5,2,9]

reversed_list = reverse_list(num_list)

print(reversed_list)


    