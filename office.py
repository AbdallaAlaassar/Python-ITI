class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.set_salary(emp.get_salary() - deduction)

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.set_salary(emp.get_salary() + reward)

    def check_lateness(self, empId, moveHour, velocity):
        emp = self.get_employee(empId)
        if emp:
            late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, velocity)
            if late:
                self.deduct(empId, 10)
                print("Employee is late. Salary deducted.")
            else:
                self.reward(empId, 10)
                print("Employee is on time. Salary rewarded.")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            print("Error: Velocity is zero. Cannot calculate lateness.")
            return True
        time_needed = distance / velocity
        arrival_hour = moveHour + time_needed
        return arrival_hour > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num