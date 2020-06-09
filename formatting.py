# person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)

tag = 'h1'
text = 'This is a headline'

sentence = '<{0}><{1}></{0}>'.format(tag, text)
print(sentence)

# class Person():

#     def __init_(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person('Jack', '33')

# sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence)

first_name = 'Corney'
last_name = 'Schafer'

# sentence = 'My name is {} {}'.format(first_name, last_name)
# print(sentence)

# sentence = f'My name is {first_name.upper()} {last_name}'
# print(sentence)

# person = {'name': 'Jenn', 'age': 23}
# # sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
# sentence = f"My name is {person['name']} and  I am {person['age']} years old."
# print(sentence) 

 
# calculation = f'4 times 11 is equal to {4*11}'
# print(calculation)


# for n in range(1, 11):
#     sentence = f'The value is {n:02}'
#     print(sentence)

# pi = 3.14159265

# sentence = f'Pi is equal to {pi:.4f}'
# print(sentence)

from datetime import datetime

birthday = datetime(1990, 1, 1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)