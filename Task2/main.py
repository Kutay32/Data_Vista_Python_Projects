import csv
import os

# Base Class: Employee
class Employee:
    def __init__(self, first_name, last_name, id_num, department):
        self.first_name = first_name
        self.last_name = last_name
        self.__id_num = id_num  # Encapsulation
        self.__salary = 0  # Encapsulation
        self.department = department
        self.vacation_days = 14  # Annual vacation days

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def apply_raise(self, rate):
        self.__salary += self.__salary * rate

    def add_bonus(self, amount):
        self.__salary += amount

    def request_vacation(self, days):
        if days <= self.vacation_days:
            self.vacation_days -= days
            return f"{days} days vacation taken. Remaining vacation days: {self.vacation_days}"
        else:
            return f"Not enough vacation days. Remaining vacation days: {self.vacation_days}"

    def show_info(self):
        return f"Employee: {self.first_name} {self.last_name}, ID: {self.__id_num}, Department: {self.department}"

# Derived Class: Full Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, id_num, department, monthly_salary):
        super().__init__(first_name, last_name, id_num, department)
        self.monthly_salary = monthly_salary
        self.set_salary(self.monthly_salary)
        self.vacation_days = 20  # Full-time employees get more vacation days

    def show_info(self):
        return f"{super().show_info()}, Monthly Salary: {self.get_salary()}"

# Derived Class: Part Time Employee
class PartTimeEmployee(Employee):
    def __init__(self, first_name, last_name, id_num, department, hourly_rate, work_hours):
        super().__init__(first_name, last_name, id_num, department)
        self.hourly_rate = hourly_rate
        self.work_hours = work_hours
        self.set_salary(self.hourly_rate * self.work_hours)
        self.vacation_days = 10  # Part-time employees get fewer vacation days

    def show_info(self):
        return f"{super().show_info()}, Weekly Salary: {self.get_salary()}"

# Derived Class: Consultant
class Consultant(Employee):
    def __init__(self, first_name, last_name, id_num, department, project_fee):
        super().__init__(first_name, last_name, id_num, department)
        self.project_fee = project_fee
        self.set_salary(self.project_fee)

    def show_info(self):
        return f"{super().show_info()}, Project Fee: {self.get_salary()}"

# Derived Class: Manager
class Manager(Employee):
    def __init__(self, first_name, last_name, id_num, department, monthly_salary):
        super().__init__(first_name, last_name, id_num, department)
        self.set_salary(monthly_salary)
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def show_employees(self):
        if not self.employee_list:
            return "No employees under this manager."
        return [employee.show_info() for employee in self.employee_list]

    def show_info(self):
        return f"{super().show_info()}, Manager, Monthly Salary: {self.get_salary()}"

# Department Class
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.csv_import()  # When a department is created, we import employees from CSV

    def add_employee(self, employee):
        self.employees.append(employee)
        self.csv_export()  # Automatically export to CSV when an employee is added

    def department_info(self):
        return f"Department: {self.name}, Number of Employees: {len(self.employees)}"

    def monthly_salary_cost(self):
        total_cost = sum(employee.get_salary() for employee in self.employees)
        return f"Total monthly salary cost for {self.name} department: {total_cost} USD"

    # CSV export function
    def csv_export(self, filename='employees.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['First Name', 'Last Name', 'ID', 'Department', 'Salary', 'Vacation Days', 'Employee Type'])
            for employee in self.employees:
                employee_type = type(employee).__name__
                writer.writerow([employee.first_name, employee.last_name, employee._Employee__id_num, 
                                 employee.department, employee.get_salary(), employee.vacation_days, employee_type])

    # CSV import function
    def csv_import(self, filename='employees.csv'):
        if os.path.exists(filename):
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    first_name = row['First Name']
                    last_name = row['Last Name']
                    id_num = int(row['ID'])
                    department = row['Department']
                    salary = float(row['Salary'])
                    vacation_days = int(row['Vacation Days'])
                    employee_type = row['Employee Type']

                    # Create appropriate employee objects based on employee type
                    if employee_type == 'FullTimeEmployee':
                        employee = FullTimeEmployee(first_name, last_name, id_num, department, salary)
                    elif employee_type == 'PartTimeEmployee':
                        employee = PartTimeEmployee(first_name, last_name, id_num, department, salary / 40, 40)  # Recalculate based on hourly rate
                    elif employee_type == 'Consultant':
                        employee = Consultant(first_name, last_name, id_num, department, salary)
                    elif employee_type == 'Manager':
                        employee = Manager(first_name, last_name, id_num, department, salary)

                    # Set vacation days from CSV
                    employee.vacation_days = vacation_days

                    # Add employee to the department
                    self.employees.append(employee)

# Example Usage:

# Create Engineering department
engineering = Department("Engineering")

# Add a full-time employee
emp1 = FullTimeEmployee("John", "Doe", 101, "Engineering", 5000)
engineering.add_employee(emp1)

# Add a manager to Engineering
manager1 = Manager("Alice", "Smith", 104, "Engineering", 10000)
engineering.add_employee(manager1)

# Add employees under manager
manager1.add_employee(emp1)

# Create a second department: Marketing
marketing = Department("Marketing")

# Add employees to the Marketing department
emp2 = PartTimeEmployee("Sara", "Johnson", 201, "Marketing", 20, 25)  # 20 USD/hour, 25 hours per week
marketing.add_employee(emp2)

consultant1 = Consultant("Bob", "Williams", 202, "Marketing", 3000)
marketing.add_employee(consultant1)

# Show info
print("Manager info:", manager1.show_info())
print("The employee that managed by the Manager:",manager1.show_employees())

# Calculate the total monthly salary cost for both departments
print(engineering.monthly_salary_cost())
print(marketing.monthly_salary_cost())

# CSV file will be created and employees will be exported
engineering.csv_export()  # If no filename is provided, 'employees.csv' is used by default
marketing.csv_export()  # You can also export for other departments
