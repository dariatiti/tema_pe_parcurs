class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_employee(self):
        print(f"Name : {self.name}, Salary: {self.salary}")

    def display_emp_count(self):
        print(f"Total number of employee(s) is {Employee.emp_count}")


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, tasks, department):
        super().__init__(name, salary)
        self.tasks = tasks
        self.department = "F08 " + department
        Manager.mgr_count += 1

    def display_employee(self):
        print(f"Departament: {self.department}")

    def display_mgr_count(self):
        print(f"Număr total de manageri: {Manager.mgr_count}")


if __name__ == "__main__":
    manager1 = Manager("Daria T.", 5000, {"Recrutare": "In Progress"}, "HR")
    manager2 = Manager("Nicoleta T.", 6000, {"Raportare": "New"}, "Finance")

    angajat = Employee("Ion Popescu", 3000)

    print("--- Afișare Manageri (Logica X%4=2: Doar Departament) ---")
    manager1.display_employee()
    manager2.display_employee()

    print("\n--- Afișare Angajat Standard (Metoda originală) ---")
    angajat.display_employee()

    print("\n--- Contori ---")
    angajat.display_emp_count()
    manager1.display_mgr_count()