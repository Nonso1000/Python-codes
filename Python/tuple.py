# myTuple = ("rose", "tulip", "sunflower")
# print(myTuple)
# myTuple2 = 1, .5, 2.,.25
# print(myTuple2)
# emptyTuple = ()
#
# # combine tuples
# finalTuple = myTuple + ("moringa", "hibiscus")
# print(finalTuple)

#Check Length
# print(len(finalTuple))

# constructor way of creating tuples
anotherTuple = tuple(("IVM", "Honda"))
print(anotherTuple)
tupleconversion = list(anotherTuple)
tupleconversion[0]="Benz"
anotherTuple= tuple(tupleconversion)
print(anotherTuple)

#Unpacking a tuple
