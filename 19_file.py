#f = open('file.txt','mode')
f = open('sample.txt')  #--> by default: read mode
# data = f.read()

a = f.read(3)   #--> first 3 char will read
# print(data)
print(a)
f.close()

#readline
f = open('sample.txt')
data = f.readline()     #read first line
print(data)

data = f.readline()     #read sec line
print(data)

data = f.readline()     #read first line
print(data)

data = f.readline()     #read sec line
print(data)

f.close()
