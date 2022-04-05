
# i = 1

# while i < 10:
#     print("Hello World " + str(i))
#     i += 1


# print("This program displays a famous movie quotaion.")

# responses = ('1', '2', '3')
# response = '0'
# while response not in responses:
#     response = input("Enter 1, 2, or, 3: ")
#     if response == '1':
#         print("Plastic.")
#     elif response == '2':
#         print("Rosebud.")
#     elif response == '3':
#         print("That's all folks.")

# count = 0  # Number of non-negative numbers input
# total = 0  # Sum Sum of non-negative numbers input

# print("(Enter -1 to terminate program.)")
# num = eval(input("Enter a non-negative number: "))
# min = num
# max = num
# while num != -1:
#     count += 1
#     total += num
#     if num < min:
#         min = num
#     if num > max:
#         max = num
#     num = eval(input("Enter a non-negative number: "))

# if count > 0:
#     print("Minimum:", str(min))
#     print("Maximum:", str(max))
#     print("Average:", str(total/count))
# else:
#     print("No non-negative numbers were entered")


# number_of_years = 0 
# balance = eval(input("Enter intial deposit: "))
# rate = eval(input("Enter the rate of return: "))
# while balance < 1000000:
#     balance += rate * balance
#     number_of_years += 1
# print("In", str(number_of_years), "years you will have a million dollars.")

list1 = []
while True:
    num = eval(input("Enter a nonnegative number: "))
    if num == -1:
        break
    list1.append(num)