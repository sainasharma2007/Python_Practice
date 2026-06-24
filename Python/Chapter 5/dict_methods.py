marks={
    "Saina":96,
    "Kartike":99,
    "Kanav":45,
    "Rishika":33
}

# items()
print(marks.items())

# keys()
print(marks.keys())

# values()
print(marks.values())

# get()
print(marks.get("Kanav"))

# update()
marks.update({"Sona":100})
print(marks)

marks.update({"Saina":92,"Kartike":95})
print(marks)

# pop()
marks.pop("Rishika")
print(marks)

# clear()
marks.clear()
print(marks)

