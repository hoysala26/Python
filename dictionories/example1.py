student = {
    "name" : "hoysala",
    "age" : 21,
    "course" : "python"
}
print(student["name"])
print(student.get("email"))
student["email"]="h@gmail.com"
print(student)
print(student.pop("course"))
student.update({"age":2,"city":"sf"})

print(student)