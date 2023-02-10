#List & Python
bicycles=['trek','cannondale','redline','specialized']
for items in bicycles:
    print(items.title())
#Last item on the List
print(bicycles[-1])

#Message
message="My first bicycle was a "+bicycles[0].title()+"."
print(message)

#Try it yourself
names=['nixchal', 'nabin', 'babain', 'shreyam', 'ramraj', 'shrawak', 'dipendra']
for name in names:
    print(name.title())
    print("Hello "+name.title()+", how are you doing today?")

#Changing/Modifying Lists
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#Use del when you want to remove value from list and not use it
#Use pop when you want to use the value later
motorcycles.remove('yamaha')
print(motorcycles)
#The remove method deletes only the first occurrence of the value you specify

#Try it yourself
guests=['luffy', 'zoro', 'sanji', 'ussop', 'nami', 'chopper', 'robin', 'franky', 'brook']
for guest in guests:
    print("You are invited to my dinner "+guest.title()+".")
print("Zoro can't make it to dinner because he is lost.")
guests.remove('zoro')
guests.insert(0,'carrot')
for guest in guests:
    print("You are invited to my dinner "+guest.title()+".")
print("I have found a bigger dinner table.")
guests.insert(0,'momo')
guests.insert(int(len(guests)/2),'yamato')
guests.append('zoro')
for guest in guests:
    print("You are invited to my dinner "+guest.title()+".")
print("I can only invite two people for dinner.")
for i in range(2,len(guests)):
    popped_guest=guests.pop()
    print("Sorry "+popped_guest.title()+", I can't invite you to dinner.")

#Organizing a List
cars=['bmw','audi','toyota','subaru']
cars.sort()