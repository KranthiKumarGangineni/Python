# ICP4


class Employee:
    """Employee Count - Data Member"""
    employeeCount = 0

    def __init__(self, employeedt):
        """Constructor to get the Dictionary and set the Required Details"""
        self.emp_details = employeedt
        self.employeeCount = len(employeedt)
        # Calling Display Method to print the Required Details
        self.display_employee_details()

    def display_employee_details(self):
        print("Total Number of Employees --> ", self.employeeCount)
        # Initializing employeeSalary variable to get the total employee salaries and finally get the average.
        employeeSalary = 0
        # Looping the Dictionary until the dictionary range
        for count in range(len(self.emp_details)):
            employeeSalary = employeeSalary + float(self.emp_details.get(count)[2])
            print("Employee %s Details :" % str(count+1))
            print("Employee Name : %s, Employee Family : %s, Employee Salary : %f, Employee Department : %s "
                  % (str(self.emp_details.get(count)[0]), str(self.emp_details.get(count)[1]),
                    float(self.emp_details.get(count)[2]), str(self.emp_details.get(count)[3])))
        print("Employees Average Salary: %f " % (employeeSalary/self.employeeCount))


class FullTimeEmployee(Employee):
    """Inherited Class"""
    print("Calling from Full Time Employee Class")
    print("-------------------------------------")
    # Creating Dictionary to call Parent Class
    employeedt = {0: ["Kranthi", "Gangineni", float(2322.45), "CSE"], 1: ["Kumar", "Gangineni", float(2312.45), "CSE"]}
    employee = Employee(employeedt)
    print("Call from Full Time Employee is Finished")
    print("----------------------------------------")

    """Constructor of Inherited Class"""
    def __init__(self, employeedt):
        Employee.__init__(self, employeedt)


moreData = "yes"
employeeInfo = {}
empId = 0
# Looping the Inputs until user specifies there are no more
while moreData[0] == 'y':
    print("Enter Below Details to get some Info")
    empName = input("Please Enter Employee Name: ")
    empFamily = input("Please Enter Employee Family: ")
    empSalary = input("Please Enter Employee Salary: ")
    empDepartment = input("Please Enter Employee Department: ")
    # Saving the Details into a Dictionary
    employeeInfo[empId] = [empName, empFamily, empSalary, empDepartment]
    empId += 1
    moreData = input("Do u have more numbers(yes or no)? ")

# Calling Employee init method.
empFinal = Employee(employeeInfo)
