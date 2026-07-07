def greet (name ,greeting = "hello"):
    print(f"{greeting} {name}")
greet("world", "hi")

def get_status (nums):
    return min(nums), max(nums), sum(nums)
low, high, total = get_status([1,2,3,4,5])
print(low, high, total)