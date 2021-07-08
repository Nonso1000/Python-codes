#Sequence Data types
mylist =['benz', 'honda', 'prada']
print (mylist)

#List Constructor method
mylist2 =(('benz', 'honda', 'prada'))
print (mylist2)
print(type(mylist))

# using membership operators on lists
print("Toyota" in mylist)
print("The first item in my list is", mylist[0])
print("The first item in my list is", mylist[-1])
print("The first item in my list is", mylist[1])

# changing list items
mylist[1] = "toyota"
print (mylist)

mylist[0:2] = ["Volvo", "Porshe"]
print (mylist)

mylist2 = mylist.copy()
print(mylist2)

# Append to a list
mylist.append("truck")
print(mylist)

#Extend a list
ourlist = ["apple", "banana", "mango"]
ourlist2 =["apricot", 'kiwi']
ourlist.extend(ourlist2)
print(ourlist)

#pop
ourlist.pop()
print(ourlist)


#delete a list item
del ourlist[0]
print(ourlist)

#sort a list
mylist.sort(reverse= True)
print(mylist)


mylist.sort()
print(mylist)
print()
welcomeMsg = "Hello World"[::-1]
# mess = welcomeMsg.split(' ')
# mess.sort(reverse=True)
print(welcomeMsg)


