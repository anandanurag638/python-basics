# 7. Create a dictionary
# 8. Add(append) elements to a dictionary
# 9. Remove(pop) elements from a dictionary
# 10. Print all keys and values of a dictionary
# 11. Find the value for a given key in the dictionary


#7. create a dictionary
mybio = {
    "name": "anurag anand",
    "VILLAGE": "ghosaith",
    "hobbies": "nothing",
    "likes": "food"
}
print(mybio)

#8. Add(append) elements to a dictionary

mybio = {
    "name": "anurag anand",
    "VILLAGE": "ghosaith",
    "hobbies": "nothing",
    "likes": "food"
}
mybio.update({"weight": "seventy six kilograms",
              "class": "bachlor in arts",
              "section": "e"})
print(mybio)

#9. remove elements to a dictionary

mybio = {
    "name": "anurag anand",
    "VILLAGE": "ghosaith",
    "hobbies": "nothing",
    "likes": "food"
  }
mybio.pop("name")
print(mybio)

#10.a.  Print all keys and values of a dictionary
print(mybio.keys())


mybio = {
    "name": "anurag anand",
    "VILLAGE": "ghosaith",
    "hobbies": "nothing",
    "likes": "food"
}
print(mybio.keys())

#10.b.  Print all keys and values of a dictionary

mybio = {
    "name": "anurag anand",
    "VILLAGE": "ghosaith",
    "hobbies": "nothing",
    "likes": "food"
 }
print(mybio.values())

#11. Find the value for a given key in the dictionary

mybio = {
    "name": "anurag anand",
    "VILLAGE": "ghosaith",
    "hobbies": "nothing",
    "likes": "food"
}
print(mybio["likes"])
