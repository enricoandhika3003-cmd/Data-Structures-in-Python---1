fruits = ["Apple", "Kiwi", "Orange", "Banana", "Grape"]
print(fruits[0])

fruits.append("Melon")
fruits.insert(2, "Lemon")
print(fruits)

fruits[2] = "Mango"
fruits.remove("Banana")
print(fruits)

print(len(fruits))

fruits.reverse()
print(fruits)

orange_fruits = fruits[2:4]
print(orange_fruits)

profile = {"name": "Enrico", "age": 14, "class": "Codingal"}
print(profile)

profile["name"] = "Bienve"
print(profile)

profile["country"] = "Indonesia"
print(profile)

del profile["country"]
print(profile)
print(profile.keys())
print(profile.values())

meeting = [
    ["Ms", "Kshitun", "Teacher"],
    [" ", "Enrico", "Student"],
    [" ", "Bienve", "Student"],
    [" ", "Saavi", "Student"]
]

meeting_dict = {}

for participant in meeting:
    title = participant[0]
    name = participant[1]
    role = participant[2]
    meeting_dict[title+name] = role

print("Codingal Lesson: ")
print(meeting_dict)
    