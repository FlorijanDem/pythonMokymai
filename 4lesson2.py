class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def display_info(self):
        return f'First name: {self.first_name}, Last name {self.last_name}, salary {self.salary}'
    def calculate_monthly_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, bonus):
        super().__init__(first_name, last_name, salary)
        self.bonus = bonus
    def calculate_monthly_salary(self):
        return super().calculate_monthly_salary() + self.bonus
    
class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hour_cost, hours):
        super().__init__(first_name, last_name, salary=0)
        self.hour_cost = hour_cost
        self.hours = hours
    def calculate_monthly_salary(self):
        return self.hour_cost * self.hours
    
agne = Employee("Agne", "Agnaite", 1500)
jonas = Manager("Jonas", "Jonaitis", 2000, 500)
ignas = HourlyEmployee("Ignas", "Ignaitis", 12, 160)

print(agne.calculate_monthly_salary())
print(jonas.calculate_monthly_salary())
print(ignas.calculate_monthly_salary())