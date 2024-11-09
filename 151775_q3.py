class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def total_salary_expenditure(self):
        total = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total}")

    def display_employees(self):
        print(f"Employees in {self.department_name}:")
        for employee in self.employees:
            employee.display_details()

# Interactive code example
if __name__ == "__main__":
    emp1 = Employee("Charlie", "E001", 50000)
    department = Department("IT")
    department.add_employee(emp1)
    department.total_salary_expenditure()
    department.display_employees()
