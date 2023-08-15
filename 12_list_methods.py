list1 = [2,4,2,6,35,2, 9]
list1.sort()
print(list1)
list1.reverse()
print(list1)

list1.append(3980) #--> adds at end
print(list1)

list1.insert(0, 1111)  #--> insert 1111 at index 0
print(list1)

print(list1.pop())  #--> pop ele at last idx
print(list1.pop(3)) #-->pop ele at idx 3
list1.remove(1111)  #-->remove 1111 from list