import csv
class Company :
    def __init__(self,company_name):
        self.company_name=company_name
        self.departments={}

    def add_department(self, department_name):
        new_department = Department(department_name)
        self.departments[department_name] = new_department

class Employee:
    def __init__(self, first_name, last_name, employee_id, department, salary, vacation_days, employee_type):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.vacation_days = vacation_days
        self.employee_type = employee_type

    def to_dict(self):
        return {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'Employee ID': self.employee_id,
            'Department': self.department,
            'Salary': self.salary,
            'Vacation Days': self.vacation_days,
            'Employee Type': self.employee_type
        }

class EmployeeManagementSystem:
    def __init__(self, filename='employees.csv'):
        self.filename = filename
        self.employees = []
        self.load_from_csv()

    def load_from_csv(self):
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employee = Employee(
                        row['First Name'], row['Last Name'], row['Employee ID'],
                        row['Department'], row['Salary'], row['Vacation Days'], row['Employee Type']
                    )
                    self.employees.append(employee)
            print(f"{len(self.employees)} çalışan yüklendi.")
        except FileNotFoundError:
            print(f"{self.filename} dosyası bulunamadı. Yeni bir dosya oluşturulacak.")

    def save_to_csv(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['First Name', 'Last Name', 'Employee ID', 'Department', 'Salary', 'Vacation Days', 'Employee Type']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for employee in self.employees:
                writer.writerow(employee.to_dict())
        print("Çalışanlar başarıyla CSV dosyasına kaydedildi.")

    def add_employee(self, employee):
        self.employees.append(employee)
        self.save_to_csv()

    def display_employees(self):
        for employee in self.employees:
            print(f"{employee.first_name} {employee.last_name}, ID: {employee.employee_id}, Department: {employee.department}, Salary: {employee.salary}, Vacation Days: {employee.vacation_days}, Type: {employee.employee_type}")


class Employee:
    def __init__(self, name, employment_type, salary):
        self.name = name
        self.employment_type = employment_type
        self.salary = salary
        self.vacation_days = self.set_default_vacation_days()

    def set_default_vacation_days(self):
        if self.employment_type == 'Full-Time':
            return 20
        elif self.employment_type == 'Part-Time':
            return 10
        elif self.employment_type == 'Consultant':
            return 14
        elif self.employment_type == 'Manager':
            return 14
        else:
            return 0

    def apply_for_vacation(self, days):
        if days <= self.vacation_days:
            self.vacation_days -= days
            print(f"{days} vacation days approved for {self.name}. Remaining vacation days: {self.vacation_days}")
        else:
            print(f"Not enough vacation days. {self.name} has {self.vacation_days} days available.")

    def raise_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary has been raised by {amount}. New salary: {self.salary}")

    def give_bonus(self, bonus):
        self.salary += bonus
        print(f"{self.name} received a bonus of {bonus}. New salary: {self.salary}")




