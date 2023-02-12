list_test = [9, 49, 94, 84, 81]
# print min of all numbers in the list
min_so_far = list_test[0]
for i in range(len(list_test)):
    if min_so_far > list_test[i]:
        min_so_far = list_test[i]
print(min_so_far)
