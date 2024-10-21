# Temel Çalışan Sınıfı
class Employee:
    def __init__(self, first_name, last_name, employee_id, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.__employee_id = employee_id  # Özel alan (capsulation)
        self.department = department
        self.__salary = salary  # Özel alan
        self.vacation_days = 0

    def get_employee_id(self):
        return self.__employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Maaş negatif olamaz!")

    def display_employee_info(self):
        print(f"Ad: {self.first_name} {self.last_name}")
        print(f"ID: {self.get_employee_id()}")
        print(f"Departman: {self.department}")
        print(f"Maaş: {self.get_salary()}")
        print(f"İzin Günleri: {self.vacation_days}")

# Tam Zamanlı Çalışan Sınıfı
class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, department, salary):
        super().__init__(first_name, last_name, employee_id, department, salary)
        self.vacation_days = 20  # Tam zamanlı çalışanlara özel izin günleri

# Yarı Zamanlı Çalışan Sınıfı
class PartTimeEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, department, hourly_rate, work_hours):
        super().__init__(first_name, last_name, employee_id, department, hourly_rate * work_hours)
        self.hourly_rate = hourly_rate
        self.work_hours = work_hours
        self.vacation_days = 10  # Yarı zamanlı çalışanlara özel izin günleri

    def calculate_salary(self):
        return self.hourly_rate * self.work_hours

# Danışman Sınıfı
class Consultant(Employee):
    def __init__(self, first_name, last_name, employee_id, department, project_fee):
        super().__init__(first_name, last_name, employee_id, department, project_fee)
        self.vacation_days = 14  # Danışmanlara özel izin günleri

# Yönetici Sınıfı
class Manager(Employee):
    def __init__(self, first_name, last_name, employee_id, department, salary):
        super().__init__(first_name, last_name, employee_id, department, salary)
        self.managed_employees = []  # Yöneticiye atanmış çalışan listesi
        self.vacation_days = 14

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def list_managed_employees(self):
        for employee in self.managed_employees:
            employee.display_employee_info()
