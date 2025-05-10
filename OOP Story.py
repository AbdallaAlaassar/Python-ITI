
from car import Car
from employee import Employee
from office import Office


fiat128 = Car(name="Fiat128", fuelRate=100, velocity=80)


samy = Employee(
    name="Samy",
    money=5000,
    mood="neutral",
    healthRate=80,
    emp_id=1,
    car=fiat128,
    email="samy@iti.org",
    salary=3000,
    distanceToWork=20
)


iti_office = Office(name="ITI")
iti_office.hire(samy)


samy.sleep(6)
samy.eat(2)
samy.buy(1)
samy.work(9)


emp_velocity = samy.car.get_velocity()
samy.drive()
iti_office.check_lateness(empId=1, moveHour=7.5, velocity=emp_velocity)

print("\n\u2705 Samy's Status:")
print(f"Mood: {samy._mood}")
print(f"Health Rate: {samy.get_health_rate()}")
print(f"Money Left: {samy.get_money()}")
print(f"Salary: {samy.get_salary()}")
print(f"Car Fuel Rate: {fiat128.get_fuel_rate()}%")
