#list comprehension
my_arr_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
my_result = [c for c in my_arr_list if c % 2 == 0]
print(my_result)
my_new_result = [j for j in my_arr_list if j % 2 != 0 ]
print(my_new_result)
print(my_arr_list)
