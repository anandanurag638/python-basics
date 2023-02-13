# print max of all numbers in the list
list_test = [9, 49, 94, 84, 81]
max_so_far = list_test[0]
for i in range(len(list_test)):
    if max_so_far < list_test[i]:
        max_so_far = list_test[i]
print(max_so_far)
