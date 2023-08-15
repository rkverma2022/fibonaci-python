letter = '''Dear <Name>,
Congratulation, you are selected as scientist at ISRO!
<Date>'''
name = input("Enter name: ")
date = input("enter date ") 

letter = letter.replace("Name", name)
letter = letter.replace("Date", date)
print(letter)