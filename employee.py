from person import Person

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.__salary = max(salary, 1000)
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self._mood = "happy"
        elif hours > 8:
            self._mood = "tired"
        else:
            self._mood = "lazy"

    def drive(self):
        velocity = self.car.get_velocity()
        self.car.run(velocity, self.distanceToWork)

    def refuel(self, gasAmount=100):
        self.car.refuel(gasAmount)

    def send_mail(self, to, subject, body, receiver_name):
        print(f"Sending mail to: {to}\nSubject: {subject}\nDear {receiver_name},\n{body}")

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 1000:
            self.__salary = salary

    def __str__(self):
        return f"Employee {self.name} (ID: {self.id})"