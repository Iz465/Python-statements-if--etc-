
def merge_lists(list1,list2):
    list3 = []
    for num in list1:
        if num % 2 == 0:
            list3.append(num)
    for num in list2:
        if num % 2 != 0:
            list3.append(num)
    return list3



list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]

list3 = merge_lists(list1,list2)

print(list3)