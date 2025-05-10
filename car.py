class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.__fuelRate = min(max(fuelRate, 0), 100)
        self.__velocity = min(max(velocity, 0), 200)

    def run(self, velocity, distance):
        self.__velocity = min(max(velocity, 0), 200)
        consumed = (distance / 10) * 10
        self.__fuelRate -= consumed
        self.__fuelRate = max(self.__fuelRate, 0)

        if self.__fuelRate <= 0:
            remaining_distance = distance - (self.__fuelRate / 10) * 10
            self.stop(remaining_distance)
        else:
            self.stop(0)

    def stop(self, remaining_distance):
        
        if remaining_distance > 0:
            print(f"Stopped before arrival. Remaining distance: {remaining_distance} km.")
        else:
            print("You have arrived at your destination.")

    def refuel(self, amount=100):
        self.__fuelRate = min(self.__fuelRate + amount, 100)

    def get_fuel_rate(self):
        return self.__fuelRate

    def get_velocity(self):
        return self.__velocity