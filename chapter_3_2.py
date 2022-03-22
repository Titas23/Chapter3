






# if not 90 >= 90:
#     print("Your grade is A")
# else: 
#     print("Your grade is not an A")



# num_1 = eval(input("Enter the first number: "))
# num_2 = eval(input("Enter the second number: "))
# if isinstance(num_1, str) or isinstance(num_2, str):
#     print("You need to input a number")
# else: 
#     if num_1 > num_2:
#             larger_value = num_1
#     else: 
#         larger_value = num_2
#         print("The larger value is", str(larger_value) + " ")

answer = eval(input("How many gallons does a ten-gallon hat hold? "))

if (0.5 <= answer <= 1):
    print("Good, ", end="")
else:
    print("No, ", end="")
print("it holds about 3/4 of a gallon.")
