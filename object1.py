class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email =  first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # @classmethod
    # def from_string(cls, emp_str):
    #     first, last, pay = emp_str_1.split('-')
    #     return cls(first, last, pay) 
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or  day.weekday() == 6:
            return False
        return True        

emp_1 = Employee('Robert', 'Williams', 5000000)
emp_2 = Employee('Jim', 'Carrey', 800000)

# // Example of Staticmethods
import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))

# // Finish Here

# emp_1.raise_amount = 1.05

# // Exmaple for the alternative class method constructor
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'


# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# // Finish Here





















# new_emp_1 = Employee(first, last, pay)





# Employee.set_raise_amount(1.05)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)
# print(emp_1.fullname())
# print(Employee.num_of_emps)




 


















# class variable
# Instance variable


# class student: 

#     def __init__(self, fname, lname, age, marks):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
#         self.grade = grade

#     def fullname(self):
#         return '{} {} is the full name.'.format(self.fname, self.lname)

#     def howManyYears(self):
#         return 'I am {} years old.'.format(self.age) 

#     def apply_marks(self):           


