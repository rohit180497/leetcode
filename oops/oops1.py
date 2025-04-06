class Employee:
    # speciali method/magic method/dunder method - constructor
    # __init__ - constructor method 
    def __init__(self, id, name, salary):
        print("Started executing attributes")
        self.id = id,
        self.name = name,
        self.salary = salary
        print("Finished executing attributes") 

    def travel(self, destination):
        print(f"Traveling in a bus to {destination}")

# creating object/instance of class Employee
rohit = Employee(101, "Rohit", 50000)
print(type(rohit))  # <class '__main__.Employee'>
# print(rohit.salary)
# rohit.travel("Delhi")
