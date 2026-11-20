d = {
    "name": "Appanna",
    "age": 20,
    "course": "Python"
}

print(d.keys())
print(d.values())
print(d.items())

print(d.get("name"))

print(d["age"])
print(d["course"])



d.update({"age": 21})
d.popitem()
print(d)

print(d.fromkeys(["a","b","c"],0))


#d.pop("course")
#print(d)