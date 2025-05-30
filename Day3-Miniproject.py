class Employee:

    employees = {}
    departement = set()
    def __init__(self, emp_id, name, dept, phn, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.phn = phn
        self.__salary = salary

    def adding(self):
        Employee.employees[self.name] = {
            "emp_id": self.emp_id,
            "dept": self.dept,
            "phn": self.phn,
            "salary": self.__salary
        }
        Employee.departement.add(self.dept)
        print(f"Employee {self.name} added successfully.")

    @classmethod
    def view(cls):
        if not cls.employees:
            print("No employees found.")
            return
        print("\nAll Employees:")
        for name, details in cls.employees.items():
            print(f"{name} => {details}")

    @classmethod
    def update(cls):
        name = input("Enter the name of the employee to update: ")
        if name in cls.employees:
            try:
                dept = input("Enter new department: ")
                phn = int(input("Enter new phone number: "))
                salary = int(input("Enter new salary: "))
                emp_id = cls.employees[name]['emp_id']
                Employee.departement.add(dept)

                cls.employees[name] = {
                    "emp_id": emp_id,
                    "dept": dept,
                    "phn": phn,
                    "salary": salary
                }
                print(f"Employee {name}'s information updated.")
            except ValueError:
                print("Invalid input type. Please enter correct values.")
        else:
            print("Employee not found!")

    @classmethod
    def viewDepartement(cls):
        result = []
        print("Choose department: \n", cls.departement)
        choice = input("Choose: ").lower().strip()
        
        for name, details in cls.employees.items():
            if details["dept"].lower().strip() == choice:
                result.append(name)
        
        if result:
            print(f"Employees in '{choice}' department: {', '.join(result)}")
        else:
            print(f"No employees found in '{choice}' department.")
            
def main():
    while True:
        print("\nChoose an option:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. viewDepartement")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            try:
                emp_id = int(input("Employee ID: "))
                name = input("Employee Name: ").strip()
                dept = input("Department: ").strip()
                phn = int(input("Phone Number: "))
                salary = int(input("Salary: "))
                emp = Employee(emp_id, name, dept, phn, salary)
                emp.adding()
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            Employee.view()
        elif choice == "3":
            Employee.update()
        elif choice == "4":
            Employee.viewDepartement()
        elif choice == "5":
            print("-----Exited-----")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
