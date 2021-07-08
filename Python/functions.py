def greet():
    print("Good morning")
greet()

def greet2(name):
    print("Good morning "   +  name)
greet2("Micheal")

def greet3(name1,name2):
    print("Good morning "+  name1 + " " +name2)
greet3("Michel", "chase")

#Arbiturary argument Function - *arg
def greet4(*name3):
    print("good morning "   +   name3[2])
greet4("micheal", "tony", "john")

#Keyword Argument Function - kwarg
def greet5(child1, child2, child3):
    print("THe names of the kids are " + child1 +" " +child2 +" " +child3 )
greet5(child1="emeka",child2="tony", child3="Jace")

#Arbitrary Keyword Argument function- **kwarg
def greet6(**child6):
    print("The firstname of the child:  " + child6["fname"])
greet6(fname="John", lname="Mark")

def ret1(x):
    return x*10

print(ret1(5))

#Lambda
x = lambda a:a*5
print(x(6))

y = lambda a,b : a * b
print(y(5, 50))

y = lambda a,b : print(f"Good Morning {a} {b}")
print(y('Nonso','Jack'))
