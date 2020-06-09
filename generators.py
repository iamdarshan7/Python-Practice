
# // LIst way of doing
# def Square_num(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return(result)   \
# 
# my_nums = Square_num([1,2,3,4,5])
# print(my_nums) 

# // Generator way of doing
# def Square_num(nums):
#     for i in nums:
#         yield(i*i)

# my_nums = Square_num([1,2,3,4,5])

# for num in my_nums:
#     print(num)

# // list Comprehension way of doing the same thing

my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)
for num in my_nums:
    print(num) 
   