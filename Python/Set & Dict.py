#Dictionaries
car={
    "name": "ford",
    'color': "red",
    "year": 2019
}
#Accessing a Dictionary
print(car["color"])
print(car.get("color"))

#Update or Change items
car["year"]=2021
print(car)

car.update({"year": 2020})


#Get Keys
print(car.values())
car['price'] = 500000
print(car.values())

#Get Items
print(car.items())
car["country"] = "Nigeria"
print(car.items())

print("model" in car)
print("prince" not in car)

#remove items
car.pop("price")
print(car)
car.clear()


#copy a Dictionary
auto = dict(car)
# auto = car.copy()
print(auto)

std1= {
    "firstname": "Rob",
    "lastname": "Jackson",
    "age": 18,
    "class": "JSS3"
}
std2= {
    "firstname": "John",
    "lastname": "Stewart",
    "age": 17,
    "class": "JSS2"
}
std3 = {
    "firstname": "Paul",
    "lastname": "Mattins",
    "age": 19,
    "class": "SS1"
}
records = {
    "student1": std1,
    "student2": std2,
    "student3": std3
}
print(records)