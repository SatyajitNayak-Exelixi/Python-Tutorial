# Dictionaries are mutable.
d = {} #This is am empty directory.

marks = {
    "Rahul": 100,
    "Somali" : 100
}

# print(marks, type(marks))
print(marks["Somali"]) #This will return NONEERROR if key is not available .
print(marks.items())
print(marks.get('Somali')) #This will return NONE if ket is not available .