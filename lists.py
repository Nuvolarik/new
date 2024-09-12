food = ["banana", "pineapple", "strawberry"]
print(food[1])
food[1] = "peach"
print(food)

food.append(True)
print(food)

food.extend("string")
print(food)

food.extend(["string", 3])
print(food)

food.remove("banana")
print(food)

print("coconut" in food)

print(food[0:2:2])

