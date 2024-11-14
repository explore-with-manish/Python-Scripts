import itertools

class IdGenerator:
    _id_counter = itertools.count(1)

    @staticmethod
    def generate_id():
        return next(IdGenerator._id_counter)
    
class Identity:
    def __init__(self):
        self.employee_id = IdGenerator.generate_id()

    def display(self):
        print(f"Employee ID: {self.employee_id}")

class Employee:
    def __init__(self, name, dob, address):
        self.name = name  # Personal name
        self.dob = dob  # Date of birth
        self.address = address  # Personal address
        self.idCard = Identity()

    def display_employee(self):
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"DOB: {self.dob}")
        print(f"Personal Address: {self.address}")
        self.idCard.display()

class Project:
    def __init__(self, project_name, manager):
        self.project_name = project_name
        self.project_id = IdGenerator.generate_id() 
        self.manager = manager

    def display_project(self):
        print(f"\nProject: {self.project_name} (ID: {self.project_id})")
        print("Managed by:")
        self.manager.display_employee()

manager = Employee("Alice", "1990-01-01", "123 Main St")

project = Project("AI Development", manager)
project.display_project()

del project

manager.display_employee()