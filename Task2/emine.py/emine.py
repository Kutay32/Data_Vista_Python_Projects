import csv

class Employee:
    def _init_(self, first_name, last_name, employee_id, department, salary, leave_days):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.leave_days = leave_days

    def update_salary(self, new_salary):
        """Updates the employee's salary."""
        self.salary = new_salary
        print(f"Salary updated: {self.salary}")

    def apply_raise(self, percentage):
        """Applies a percentage-based raise to the employee's salary."""
        self.salary += self.salary * (percentage / 100)

    def take_leave(self, days):
        if days <= self.leave_days:
            self.leave_days -= days
            print(f"You took {days} days off. Remaining leave days: {self.leave_days}")
        else:
            print("You don't have enough leave days!")

class FullTime(Employee):
    def _init_(self, first_name, last_name, employee_id, department, salary):
        super()._init_(first_name, last_name, employee_id, department, salary, leave_days=20)

class PartTime(Employee):
    def _init_(self, first_name, last_name, employee_id, department, hourly_wage, work_hours):
        salary = hourly_wage * work_hours
        super()._init_(first_name, last_name, employee_id, department, salary, leave_days=10)
        self.hourly_wage = hourly_wage
        self.work_hours = work_hours

class Consultant(Employee):
    def _init_(self, first_name, last_name, employee_id, department, project_fee):
        super()._init_(first_name, last_name, employee_id, department, project_fee, leave_days=14)

class Manager(Employee):
    def _init_(self, first_name, last_name, employee_id, department, salary):
        super()._init_(first_name, last_name, employee_id, department, salary, leave_days=14)
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)
        print(f"{employee.first_name} {employee.last_name} has been added to your subordinates.")
    
    def view_subordinates(self):
        for employee in self.subordinates:
            print(f"- {employee.first_name} {employee.last_name}")

def load_csv(file_name):
    employees = []
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    if row['EmployeeType'] == 'FullTime':
                        employee = FullTime(row['FirstName'], row['LastName'], row['EmployeeID'], row['Department'], float(row['Salary']))
                    elif row['EmployeeType'] == 'PartTime':
                        employee = PartTime(row['FirstName'], row['LastName'], row['EmployeeID'], row['Department'], float(row['HourlyWage']), float(row['WorkHours']))
                    elif row['EmployeeType'] == 'Consultant':
                        employee = Consultant(row['FirstName'], row['LastName'], row['EmployeeID'], row['Department'], float(row['ProjectFee']))
                    elif row['EmployeeType'] == 'Manager':
                        employee = Manager(row['FirstName'], row['LastName'], row['EmployeeID'], row['Department'], float(row['Salary']))
                    else:
                        raise ValueError(f"Unknown employee type: {row['EmployeeType']}")
                    employees.append(employee)
                except KeyError as e:
                    print(f"Missing data in row: {e}, Row: {row}")
                except ValueError as e:
                    print(f"Data error: {e}, Row: {row}")
        print("Data loaded.")
    except FileNotFoundError:
        print("CSV file not found, a new file will be created.")
    return employees

def save_csv(file_name, employees):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['FirstName', 'LastName', 'EmployeeID', 'Department', 'Salary', 'LeaveDays', 'EmployeeType', 'HourlyWage', 'WorkHours', 'ProjectFee']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            row = {
                'FirstName': employee.first_name,
                'LastName': employee.last_name,
                'EmployeeID': employee.employee_id,
                'Department': employee.department,
                'Salary': employee.salary,
                'LeaveDays': employee.leave_days
            }
            if isinstance(employee, FullTime):
                row['EmployeeType'] = 'FullTime'
            elif isinstance(employee, PartTime):
                row['EmployeeType'] = 'PartTime'
                row['HourlyWage'] = employee.hourly_wage
                row['WorkHours'] = employee.work_hours
            elif isinstance(employee, Consultant):
                row['EmployeeType'] = 'Consultant'
                row['ProjectFee'] = employee.salary
            elif isinstance(employee, Manager):
                row['EmployeeType'] = 'Manager'
            writer.writerow(row)
        print("Data saved.")

if _name_ == "_main_":
    file_name = "employees.csv"
    employee_list = load_csv(file_name)

    # Save the data
    save_csv(file_name, employee_list)

    # Employee operations
    new_employee.take_leave(5)
    new_employee.update_salary(150000)
