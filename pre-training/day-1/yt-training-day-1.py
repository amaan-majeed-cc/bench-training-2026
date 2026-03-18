# print("Amaan Majeed")

# print("o-----")
# print(" ||||")

# print("*" * 10)


# price = 10
# print(price)

# rating = 4.9
# name = "Amaan Majeed"
# is_published = True


# name = "John Smith"
# age = 20
# is_new = True


# name = input("What is your name? ")
# print("Hi " + name)

# name = input("What is your name? ")
# color = input("What is your favourite color? ")
# print(name + " likes " + color)

# birth_year = input("Birth Year: ")
# age = 2026 - int(birth_year)
# print(type(age))
# print(age)


# weight_lbs = input("Weight (lbs): ")
# weight_kg = float(weight_lbs) * 0.45
# print(weight_kg)


# course = 'Python for "Beginners"'
# print(course)

# course = "Python for Beginners"
# another = course[:3]

# print(another)


# ### Formatted Strings
# first = "Amaan"
# last = "Majeed"

# message = first + " [" + last + "] is a coder"
# msg = f"{first} [{last}] is a coder"
# print(message)
# print(msg)


# course = "Python for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find("P"))
# print(course.find("o"))
# print(course.replace("Beginners", "Absolute Beginners"))
# print(course.replace("P", "J"))


# ### Arithmetic Operators
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)


# x = 10
# x = x + 3
# print(x)

# x = 10
# x += 3
# print(x)

# x = 10 + 3 * 2 ** 2
# print(x)


# x = (2 + 3) * 10 - 3
# print(x)


# ### Math Functions

# import math

# print(math.ceil(2.9))
# print(math.floor(2.9))
# x = 2.9
# print(round(x))



# ### If Statements

# is_hot = True
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")
# print("Enjoy your day")

# hourse_price = 1_000_000
# credit_good = True

# if credit_good:
#   print("Down Payment: ", hourse_price * 0.1)
# else:
#   print("Down Payment: ", hourse_price * 0.2)



### Logical Operator

# has_high_income = True
# has_good_credit = True

# if has_high_income or has_good_credit:
# 	print("Eligible for loan")


# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
# 	print("Eligible for loan")


### Comparison Operators

# temperature = 30

# if temperature > 30:
#   print("It's a hot day")
# else:
#   print("It's not a hot day")


# name = "Amaan"

# if len(name) < 3:
#   print("Name must have at least 3 characters")
# elif len(name) > 50:
#   print("Name can be maximum of 50 characters")
# else:
#   print("Name looks good!")



# ### Weight converter

# weight = int(input("Weight: "))
# conversion = input("(L)bs or (K)gs: ")

# if conversion.upper() == "L":
#   print(f'You are {weight * 0.45}')
# elif conversion.upper() == "K":
#   print(f'You are {weight / 0.45}')


### While Loops

# i = 1
# while i <= 5:
#   print("*" * i)
#   i += 1
# print("Done")

### Guessing game

# secret_number = 9
# tries = 0
# number = 0
# while tries < 3 and number != secret_number:
#   number = int(input(f'Guess {tries + 1}: '))
#   tries += 1

# if number != secret_number:
#   print("Sorry you Failed!")
# else:
#   print("You passed")


### Car Game
# command = ''
# started = False
# while True:
# 	command = input("> ").lower()
# 	current_state = command
# 	if command == "start":
# 		if started:
# 			print("Car Already started...")
# 		else:
# 			print("Car started...")
# 			started = True
# 	elif command == "stop":
# 		if started:
# 			print("Car stopped.")
# 			started = False
# 		else:
# 			print("Car is Already stopped")
# 	elif command == "help":
# 		print("""
# start - to start the car
# stop - to stop the car
# quit - to exit
# 					"""
# 				)
# 	elif command == "quit":
# 		break
# 	else:
# 		print("Sorry, I don't understand that!")



### For Loop

# for item in "Python":
# 	print(item)

# for item in ["Amaan", "Majeed", "Python"]:
# 	print(item)

# for item in [1, 2, 3, 4, 5]:
# 	print(item)

# for item in range(5, 10):
# 	print(item)


# prices = [10, 20, 30]

# sum = 0
# for item in prices:
#   sum += item

# print("Sum: ", sum)


# for x in range(4):
# 	for y in range(3):
# 		print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#   print('x' * i)


for i in range(len(numbers)):
	for j in range(numbers[i]):
		print("x", end='')
	print('')

