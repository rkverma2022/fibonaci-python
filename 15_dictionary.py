myDict = {
    'key': 'value',
    'fast': "393",
    'marks': 49,
    1:5
}
print(myDict['fast'])
print(myDict['key'])

#mutable
myDict['marks'] = [3,5,2]
print(myDict['marks'])

#dictionary method
print(myDict.keys())

print(myDict.values())

print(myDict.items())

update_dic ={'hello': 90848,
'fast': 7389}
myDict.update(update_dic)       #update the dict

#.get()
print(myDict.get('fast3'))   #if key is not present -->it return none
#print(myDict['fast1'])      #throw an error

print(myDict)
#typecasting
print(type(myDict))

print(list(myDict))

print(myDict)


