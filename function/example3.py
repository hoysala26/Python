def greet (name ,greeting = "hello"):
    print(f"{greeting} {name}")
greet("world", "hi")

def get_status (nums):
    return min(nums), max(nums), sum(nums)
low, high, total = get_status([1,2,3,4,5])
print(low, high, total)

square = lambda x: x * x
print(square(5))

def add(*args):
    total = 0

    for num in args:
        total += num

    print(total)