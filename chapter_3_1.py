"""
Relational Operator 
<, <=, >, >=, !=, == 

Logical Operator
and, or, not, in, not in 
"""

# # true_or_false = "b" > "a"
# true_or_false = not ("!" > "z" or "b" > "a")
# print("True or False: ",true_or_false)

# numbers_1 = [3,5] < [3,7]
# numbers_2 = [3,5] < [3,5,6]
# numbers_3 = [3,5,7] < [3,7,2]
# numbers_4 = [7,"three", 5] < [7,"two", 2]

# print()
# print()
# print()
# print()

# variable = ("a+b") < ("2*a")

# print(variable)

# variable_2 = ["(len(c)-b" == ("a/2")]

# print(variable_2)

# variable_3 = "c" < "good" + "d"

# print(variable_3)

# list1 = [6, 4, -5, 3.5]

# print(list1)
# list1.sort()

# print(list1)

# list2 = ["ha", "hi", 'B', '7']

# list2.sort()
# print(list2)


# list1 = [chr(177), "cat", "car", "Dog", "dog", "8-ball", "5", chr(162)]
# list1.sort()
# print(list1)

# monarchs = [("George", 5), ("Elizaeth", 2), ("George", 6), ("Elizabeth", 1)]
# monarchs.sort()
# print(monarchs)


state = "CA"
states = ["MD", "VA", "WV", "DE"]

is_in_list = state in states 

print(not(not(is_in_list) and "VA" in states))