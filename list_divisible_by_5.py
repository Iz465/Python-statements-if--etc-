
def divisible(list1,list2):
    list3 = []
    for num in list1:
        list2.append(num)
    for num in list2:
        if num % 5 == 0:
            list3.append(num)
        elif num % 5 == 1:
            list3.append(num)
    list3.sort()
    return list3




numbered_list = [11,21,29,25,31,41,39,49, 50] # 11,21,25,41,50
numbered_list1 = [13,24,20,35,99,57,43,51] # 20,35,51

result_list = divisible(numbered_list, numbered_list1)

print(result_list)

