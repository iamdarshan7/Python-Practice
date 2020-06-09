# import re

# text_to_search = '''
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890

# Ha HaHa

# MetaCharacters (Need to be escaped):
# . ^ $ * + { } [ ] \ | ( )

# coreyms.com

# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234

# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T


# cat 
# mat
# pat 
# bat

# '''

# sentence = 'Start a sentence and then bring it to an end'

# # print(r'\tTab')

# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-z]\w*')

# matches = pattern.finditer(text_to_search)

  
# for match in matches:
#     print(match)

# # with open('data.txt', 'r') as f:
# #     contents = f.read()

# #     matches = pattern.finditer(contents)

# #     for match in matches:
# #         print(match)
  

# # print(text_to_search[104:108])


# // Classwork 1

# import re

# emails = '''
# CoreyMSchafer@gmail.com
# Corey.schafer@university.edu
# Corey-321-schafer@my-work.net
# '''

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')

# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

# // ClassWork 2

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'(https?)://(www\.+)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)


# subbed_urls = pattern.sub(r'\2\3',urls)

# print(subbed_urls)
for match in matches:
    print(match.group(3))
    # sentence = f'This is {match.group(2)}'
    # print(sentence)