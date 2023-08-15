b = set()
b.add(4)
b.add(5)
print(type(b))
print(b)

#-->can't add list --> because it is mutable
# c = {[3,5],2}
#-->can't add dict-->mutable
# d = {{'key':'value'}}

#-->tuple is immutable: can be add to set
e = {(2,3),(2,0),()}
print(e)


#-->len of set
print(len(e))

#-->remove
# e.remove(3) #-->error
e.remove(())
print(e)

print(e.pop())

f = {3,5,6,2}
print(e.union(f))
print(e.intersection(f))

#-->clear set  
print(e.clear())