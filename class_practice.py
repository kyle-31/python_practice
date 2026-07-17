class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"員工名子{self.name},員工工號{self.id}")

    
class FullTimeEployee(Employee):
    def __init__(self , name , id , monthly_salary):
        super().__init__(name , id)
        self.monthly_salary = monthly_salary

    def calculate_monthy_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self , name , id , daily_salary , work_days):
        super().__init__(name , id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthy_pay(self):
        return self.daily_salary * self.work_days

employee_1 = FullTimeEployee("員工1" , "001" , 29500)
employee_2 = PartTimeEmployee("員工2" , "002" , 1200 , 15)

employee_1.print_info()
employee_2.print_info()

print(employee_1.calculate_monthy_pay())
print(employee_2.calculate_monthy_pay())