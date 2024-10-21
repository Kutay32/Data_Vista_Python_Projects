from employee import FullTimeEmployee, PartTimeEmployee, Consultant, Manager
import csv

# Çalışanları CSV dosyasına kaydetme
def save_employees_to_csv(employees, filename="employees.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["First Name", "Last Name", "Employee ID", "Department", "Salary", "Vacation Days", "Employee Type"])
        for employee in employees:
            writer.writerow([employee.first_name, employee.last_name, employee.get_employee_id(),
                             employee.department, employee.get_salary(), employee.vacation_days, type(employee).__name__])

# CSV'den çalışanları yükleme
def load_employees_from_csv(filename="employees.csv"):
    employees = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Employee Type"] == "FullTimeEmployee":
                    employee = FullTimeEmployee(row["First Name"], row["Last Name"], row["Employee ID"], row["Department"], float(row["Salary"]))
                elif row["Employee Type"] == "PartTimeEmployee":
                    # Varsayılan olarak saatlik ücret ve saat bilgileri yok
                    employee = PartTimeEmployee(row["First Name"], row["Last Name"], row["Employee ID"], row["Department"], 0, 0)
                elif row["Employee Type"] == "Consultant":
                    employee = Consultant(row["First Name"], row["Last Name"], row["Employee ID"], row["Department"], float(row["Salary"]))
                elif row["Employee Type"] == "Manager":
                    employee = Manager(row["First Name"], row["Last Name"], row["Employee ID"], row["Department"], float(row["Salary"]))
                employee.vacation_days = int(row["Vacation Days"])
                employees.append(employee)
    except FileNotFoundError:
        print(f"{filename} bulunamadı, yeni bir dosya oluşturulacak.")
    return employees

# Program Başlangıcı
employees = load_employees_from_csv()

# Çalışan bilgilerini gösterme
for employee in employees:
    employee.display_employee_info()

# Çalışanları CSV dosyasına kaydetme
save_employees_to_csv(employees)
