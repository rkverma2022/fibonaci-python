with open('sample.txt') as f:
    a = f.read()
if 'Hey' in a:
    print(''''hey' is there ''')
else:
    print("not found")

with open('sample.txt','w') as f:
    f.write("Hey, do you like to kill me?")
