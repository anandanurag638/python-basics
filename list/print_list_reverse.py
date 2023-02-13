# print all elements of the list in reverse order
list_test = [9, 49, 94, 84, 81]
list_rev = []
for i in range(len(list_test)):
    list_rev.append(list_test[len(list_test) - 1 - i])
print(list_rev)

