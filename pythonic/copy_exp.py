import copy

mylist = [[1,2,3],[4,5],[6,'a']]

print("Address of mylist  : ", id(mylist))
print("Adress of first element : ", id(mylist[0]))
print("Adress of second element : ", id(mylist[1]))
print("Adress of third element : ", id(mylist[2]))

# new_list = copy.copy(mylist)
# new_list = mylist
new_list = copy.deepcopy(mylist)
print("Address of new_list  : ", id(new_list))
print("Adress of first element : ", id(new_list[0]))
print("Adress of second element : ", id(new_list[1]))
print("Adress of third element : ", id(new_list[2]))


