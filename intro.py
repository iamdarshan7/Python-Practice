# message = "Hello World"

# print(len(message))
# print(message[:5])
# print(message[6:])
# print(message[4:])
# print(message.lower())
# print(message.upper())
# print(message.count('o'))
# print(message.count('l'))
# print(message.find('World')) // to find the index of the string "World"
# message = message.replace('World', 'universe')
# print(message)

greeting = 'Hello'
name = 'Michael'

# message = greeting + ', ' + name
# Alternative way
message = '{}, {}. Welcome!'.format(greeting, name)
message1 = f'{greeting}, {name.upper()}. Welcome!'

print(message)
print(message1)
# print(dir(name))
print(help(str))