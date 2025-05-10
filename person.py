class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.__money = money
        self._mood = mood
        self.__healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self._mood = "happy"
        elif hours < 7:
            self._mood = "tired"
        else:
            self._mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.__healthRate = 100
        elif meals == 2:
            self.__healthRate = 75
        elif meals == 1:
            self.__healthRate = 50
        else:
            self.__healthRate = 0

    def buy(self, items):
        self.__money -= 10 * items

    def get_money(self):
        return self.__money

    def get_health_rate(self):
        return self.__healthRate