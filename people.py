import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', "Thomas"]
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Bussiness']

print("Memory (Before): {}Mb".format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        