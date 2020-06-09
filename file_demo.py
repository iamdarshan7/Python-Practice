# File Objects


  # // this is old method  
    # f = open('test.txt', 'r')
    # # print(f.name)
    # print(f.mode)
    # f.close()


with open('test.txt', 'r') as rf: 
    with open('test_copy.text', 'w') as wf:
        for line in rf:
            wf.write(line)



















#     size_to_read = 10
# #
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')

#     f.seek(0)

#     f_contents = f.read(size_to_read)
#     print(f_contents)

#     print(f.tell())

#     # while len(f_contents) > 0:
#     #     print(f_contents, end='*')
#     #     f_contents = f.read(size_to_read)

    
  