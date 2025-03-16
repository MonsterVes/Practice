# # 1. Write a Python script to sort (ascending and descending) a dictionary by value.
# my_dict = {}
# my_dict["apple"] = 2
# my_dict["mango"] = 4
# my_dict["pear"] = 1
# my_dict["orange"] = 5
# my_dict["grapefruit"] = 3
# my_dict["tangerine"] = 1

# # print(my_dict)

# sorted_dict = {k: v for k, v in sorted(my_dict.items(), key = lambda key: key[1])}
# print(sorted_dict)
# sorted_dict = {k: v for k, v in sorted(my_dict.items(), key = lambda key: key[1], reverse = True)}
# print(sorted_dict)

#------------------------

# # 2. Write a Python script to add a key to a dictionary.

# # Sample Dictionary : {0: 10, 1: 20}
# # Expected Result : {0: 10, 1: 20, 2: 30}

# my_dict = {0: 10, 1: 20}
# my_dict.update({2:30})
# print(my_dict)

#------------------------

# # 3. Write a Python script to concatenate the following dictionaries to create a new one.

# # Sample Dictionary :
# # dic1={1:10, 2:20}
# # dic2={3:30, 4:40}
# # dic3={5:50,6:60}
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}

# new_dict = {}
# for dict in (dic1, dic2, dic3):
#     new_dict.update(dict)

# print(new_dict)

#------------------------

# # 4. Write a Python script to check whether a given key already exists in a dictionary.

# my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# key_lookup = 12

# if key_lookup in my_dict:
#     print(f"{key_lookup} is present in my_dict")
# else:
#     print(f"{key_lookup} is NOT present in my_dict")

#------------------------

# # 5. Write a Python program to iterate over dictionaries using for loops.

# my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# for k,v in my_dict.items():
#     print(f"{k}: {v}")

#------------------------

# # 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# # Sample Dictionary ( n = 5) :
# # Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# dict_len = int(input("Enter dictionary len: "))
# my_dict = {}
# for k in range(1, dict_len+1):
#     dict_update = {k: k*k for k in range(1, dict_len+1)}
#     my_dict.update(dict_update)

# print(my_dict)

#------------------------

# # 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# # Sample Dictionary
# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# my_dict = {}
# for k in range(1, 16):
#     dict_update = {k: k*k for k in range(1, 16)}
#     my_dict.update(dict_update)

# print(my_dict)

# my_dict = {}
# for num in range(1, 16):
#     my_dict[num] = num*num
# print(my_dict)

#------------------------

# #8. Write a Python script to merge two Python dictionaries.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}

# merged_dic = dic1.copy()
# merged_dic.update(dic2)

# print(merged_dic)

#-----------------------

# #10. Write a Python program to sum all the items in a dictionary.


# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# sum_of_items = 0
# for value in my_dict.values():
#     sum_of_items += value
# print(f"sum of all items is {sum_of_items}")

# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# print(sum(my_dict.values()))

#-----------------------


# # 11. Write a Python program to multiply all the items in a dictionary.

# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

# result = 1

# for item in my_dict.values():
#     result *= item
# print(result)    