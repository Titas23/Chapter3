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

# answer = eval(input("How many gallons does a ten-gallon hat hold? "))

# if (0.5 <= answer <= 1):
#     print("Good, ", end="")
# else:
#     print("No, ", end="")
# print("it holds about 3/4 of a gallon.")

# first_num = eval(input("Enter the first number: "))
# second_num = eval(input("Enter the second number: "))
# third_num = eval(input("Enter the third number: "))

# max = first_num
# if second_num > max:
#     max = second_num
# if third_num > max:
#     max = third_num
# print("The largest number is", str(max) + ".")

# numbers = []

# first_num = eval(input("Enter the first number: "))
# second_num = eval(input("Enter the second number: "))
# third_num = eval(input("Enter the third number: "))

# numbers.append(first_num)
# numbers.append(second_num)
# numbers.append(third_num)

# print("The largest number is", str(max(numbers)) + ".")


# color = input("Enter a color (BLUE or RED): ").upper()
# mode = input("Enter a mode (STEADY or FLASHING): ").upper()

# result = ""
# if color == "BLUE":
#     if mode == "STEADY":
#         result = "Clear view."
#     else: # mode is flashing
#         result = "Clouds are Due."
# else: # color is RED
#     if mode == "STEADY":
#         result = "Rain ahead."
#     else: # mode is flashing
#         result = "Snow Ahead"
# print("The weather forecast is", result)

# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "Break even"
# else: 
#     if costs < revenue:
#         profit = revenue - costs
#         result = "Profit is ${0:.2f}.".format(profit)
#     else:
#         loss = costs - revenue
#         result = "Loss is ${0:.2f}.".format(loss)
# print(result)

# costs = eval(input("Enter total costs: "))
# revenue = eval(input("Enter total revenue: "))

# if costs == revenue:
#     result = "Break even"
# else: 
#     if costs < revenue:
#         result = " is ${0:.2f}.".format(revenue - costs)
#     if (revenue - costs) < 0:
#         result = "Loss" + result
#     else:
#         result = "Profit" + result
# print(result)

# for i in range(0,1):
#     first_num = input("Enter the first number: ")
#     second_num = input("Enter the second number: ")
# if first_num > second_num:
#     print("The larger value is", str(first_num) + ".")
# elif second_num > first_num:
#     print("The larger value is", str(second_num) + ".")
# else:
#     print("The two values are equal")

# Do example 7 in the textbook at home

str_1 = "Enter total earnings for this year prior to current pay period: "
ytd_earnings = eval(input(str_1)) #year-to-date earnings
cur_earnings = eval(input("Enter earnings for the current pay period: "))
total_earnings = ytd_earnings + cur_earnings

social_security_ben_tax = 0 
if total_earnings <= 117000:
    social_security_ben_tax = 0.062 * cur_earnings
elif ytd_earnings < 117000:
    social_security_ben_tax = 0.062 * (117000 - ytd_earnings)
# Calculate and display the FICA tax
medicare_tax = 0.0145 * cur_earnings
if ytd_earnings >= 200000:
    medicare_tax += 0.009 * cur_earnings
elif total_earnings > 200000:
    medicare_tax += 0.009 * (total_earnings - 200000)
fica_tax = social_security_ben_tax + medicare_tax
print("FICA tax for the current pay period: ${0:0,.2f}".format(fica_tax))



# Example 8 in the textbook

# gpa = eval(input("Enter your gpa: "))

# if gpa >= 3.9:
#     honors = " summa cum laude."
# elif gpa >= 3.6:
#     honors = " magna cum laude."
# elif gpa >= 3.3:
#     honors = " cum laude."
# else:
#     honors = "."
# print("You graduated" + honors)

# for i in range(0,1):
#     num_1 = input("Enter first number: ")
#     num_2 = input("Enter second number: ")
# if num_1.isdigit() and num_2.isdigit():
#     print("The sum is", str(eval(num_1) + eval(num_2)) + "." ) 
# elif not num_1.isdigit():
#     if not num_2.isdigit():
#         print("Neither entry was a proper number.")
#     else:
#         print("The first entry was not a proper number")
# else: 
#     print("The second entry was not a proper number.")

# if 7:
#     print("A nonzero number is true.")
# else:
#     print("The number zero is false.")
# if []:
#     print("A nonempty list is true.")
# else:
#     print("An empty list is false.")
# if ["spam"]:
#     print("A nonempty list is true.")
# else:
#     print("The empty list is false")

