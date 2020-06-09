# message = 'hi friends'
# another = "I'm here!"

# # print(message.capitalize())
# cool = f'{message.capitalize()} {another}'
# print(cool)

# num = '3.14'
# print(type(num))

# print(3 // 2) for floor division
# print(3 ** 2)
# print(3 * 2 + 1)
# print(3 * (2 + 1))

# num = 1
# num *= 10


# print(abs(-3))
# print(round(3.75,4))

# num_1 = 3
# num_2 = 2

# print(num_1 <= num_2)

# num_1 = '100'
# num_2 = '200'

# num_1 = int(num_1)
# num_2 = int(num_2)

# print(num_1 + num_2)

# courses = ['history', 'Math', 'Physics', 'CompSci']
# courses_2 = ['Art', 'Education']
# nums = [1, 5, 2, 4, 3]
# courses.extend(courses_2)

# courses.remove('Math')
# returned_value = courses.pop()
# print(returned_value)

# courses.reverse()
# nums.sort(reverse = True)
# print(nums)

# sorted_courses = sorted(courses)
# print(sorted_courses)

# print(min(nums))
# print(max(nums))
# print(sum(nums))

# print(courses.index("Math"))
# print("Art" in courses)
# print("Math" in courses)

#  important 
# for index, course in enumerate(courses, start= 1):
    # print(index, course)

# course_str = ' - '.join(courses)
# new_list = course_str.split(' - ')

# print(course_str)
# print(new_list)
# // concept of list in terms of mutabilitiy

# list_1 = ['History', 'Math', 'Physics', 'CompSci']

# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# // Immutabe
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# 
# print(tuple_1)
# print(tuple_2)
# 
# tuple_1[0] = 'Art'
# 
# print(tuple_1)
# print(tuple_2)


# //  sets

# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
# art_courses = {'History', 'Math', 'Art', 'Design'}


# print(cs_courses.union(art_courses))

# // how to create empty list, tuple and set

# empty_list = [] or empty_list = list()

# empty_tuple = () or empty_tuple = tuple()

# empty_set = {} // This is not right! It is dictionary
# empty_set = set()

# // Dictionary

student = {'name': 'John', "age": 25, 'courses': ['Math', 'CompSci']}

# student['phone'] = '555-5555'
# student['name'] = 'jane'

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

# age = student.pop('age')
# print(student.get('phone', 'Not FOund'))
# print(student)
# print(len(student))
# print(student.items())
for key, value in student.items():
  print(f'This is key i.e {key} and the value is {value}')