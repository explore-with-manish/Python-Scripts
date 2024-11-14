import itertools

# ID Generator: Generates unique Employee IDs
class IdGenerator:
    _id_counter = itertools.count(1)  # Infinite counter starting from 1

    @staticmethod
    def generate_id():
        return next(IdGenerator._id_counter)


# Identity Class: Represents the official identity of an Employee
class Identity:
    # Static (class-level) attributes for company details
    _company_name = "Tech Corp"
    _company_address = "456 Corporate Ave"

    def __init__(self):
        self.employee_id = IdGenerator.generate_id()  # Unique Employee ID

    # Getter for Company Name
    @classmethod
    def get_company_name(cls):
        return cls._company_name

    # Setter for Company Name
    @classmethod
    def set_company_name(cls, new_name):
        cls._company_name = new_name

    # Getter for Company Address
    @classmethod
    def get_company_address(cls):
        return cls._company_address

    # Setter for Company Address
    @classmethod
    def set_company_address(cls, new_address):
        cls._company_address = new_address

    def display(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Company: {Identity.get_company_name()}")
        print(f"Company Address: {Identity.get_company_address()}")


# Employee Class: Represents an employee with personal and official details
class Employee:
    def __init__(self, name, dob, address):
        self.name = name  # Personal name
        self.dob = dob  # Date of birth
        self.address = address  # Personal address
        # Composing Identity for the Employee
        self.identity = Identity()

    def display_employee(self):
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"DOB: {self.dob}")
        print(f"Personal Address: {self.address}")
        self.identity.display()  # Display the Employee's Identity


# Project Class: Represents a project with a single Manager (Composition)
class Project:
    def __init__(self, project_name, manager):
        self.project_name = project_name
        self.project_id = IdGenerator.generate_id()  # Unique Project ID
        self.manager = manager  # Composition: Project has one Manager

    def display_project(self):
        print(f"\nProject: {self.project_name} (ID: {self.project_id})")
        print("Managed by:")
        self.manager.display_employee()


# Demonstrating the Design
if __name__ == "__main__":
    # Modify Static Company Information
    # print("Updating Company Details...")
    # Identity.set_company_name("NextGen Tech")
    # Identity.set_company_address("789 Future St")

    # Create Employees
    emp1 = Employee("Alice", "1990-01-01", "123 Main St")
    emp2 = Employee("Bob", "1992-05-10", "789 Oak St")

    # Assign Bob as the Manager of a Project
    project = Project("AI Development", emp2)

    # Display Employee and Project Details
    emp1.display_employee()  # Alice's details
    project.display_project()  # Project managed by Bob
