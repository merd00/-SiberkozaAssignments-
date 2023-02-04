# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
person_mo = {
    "name" : "Mert",
    "surname" : "Öztürk",
    "age" : 22
}
print(person_mo)

# Get value
print(person_mo["age"])

# Add key/value
person_mo["number"] = "4568712"
print(person_mo.keys())
print(person_mo.values())
print(person_mo.items())

# Remove item
del(person_mo["age"])
person_mo.pop("number")
print(person_mo)

#Length
print(len(person_mo))

#Clear
person_mo.clear()
print(person_mo)

#List of Dict

people = [
    {"name": "Mert", "surname": "Öztürk"},
    {"name": "mrt", "surname": "Oztrk"}
]
print(people[0]["name"])