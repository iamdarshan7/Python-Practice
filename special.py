class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)   

    def __repr__(self):
        return "Employee ('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)      

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Thapa', 60000)

# print(emp_1)
print('test'.__len__())
# // both way is ok

# // 1st way
# print(repr(emp_1))
# print(str(emp_1))

# // 2nd way
# print(emp_1.__rep__())
# print(emp_1.__str__())
 
# // Finish Here 

# // Other special dunder methods

# print(int.__add__(1, 2))  // prints 3
# print(str.__add__('a', 'b')) // prints ab