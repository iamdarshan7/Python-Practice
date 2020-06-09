#  Python Object-Oriented Programming

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04 

    def __init__(self,first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      self.email = first + '.' + last + '@company.com'
      Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# print(Employee.num_of_emps)
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# print(Employee.num_of_emps)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# # print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_2.fullname())

# print('{} {}'.format(emp_1.first, emp_1.last))



# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = "User"
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000
