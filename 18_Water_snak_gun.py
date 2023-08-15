import random

def gameWin(comp, user):
    if comp == user:
        return 0
    elif comp == 's':
        if user == 'g':
            return True
        else:
            return False
    elif comp == 'w':
        if user == 's':
            return True
        else:
            return False


a = ['w', 's', 'g']

comp = a[random.randint(0, len(a)-1)]

user = input("Enter w, s, g? ")
decision = gameWin(comp, user)

print(f"computer: {comp}, user: {user}")
if decision == 0:
    print("Tie")
elif decision:
    print("Win")
else:
    print("Loose")