class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name}: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def display(self):
        super().display()
        print(f"Manages a team of {self.team_size}")

m = Manager("Alice", 90000, 5)
m.display()
