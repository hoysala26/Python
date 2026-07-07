fruits = ["mango", "banana", "apple", "orange","apple"]

fruits.append("kiwi")
fruits.insert(1,"kiwi")
fruits.remove("banana")
fruits.pop()
fruits.sort()
fruits.reverse()
print(fruits.index("mango"))
print(fruits.count("apple"))
print(len(fruits))
print("apple" in fruits)
print(fruits)

# Traditional way
squares = []
for x in range(5):
    squares.append(x * x)

# List comprehension (same result)
squares = [x * x for x in range(5)]   # [0, 1, 4, 9, 16]
print(squares)