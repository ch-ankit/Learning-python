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
