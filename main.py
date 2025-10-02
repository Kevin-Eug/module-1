# TODO: Create an integer variable named 'age' with your age
# TODO: Create a float variable named 'height' with your height in meters
# TODO: Create a string variable named 'name' with your name
# TODO: Create a boolean variable named 'is_student' and set it to True
# Print all variables and their types
# Example: print(f"Age: {age}, Type: {type(age)}")

age = 25
height = 1.91
name = "Kevin"
# is_student = True
# print(f"Name: {name}, Age: {age}, Height: {height},Is student: {is_student}")

# TODO: Create two variables 'a' and 'b' with numeric values
# TODO: Perform addition, subtraction, multiplication, and division of a and b
# Print the results of each operation
# TODO: Calculate the remainder of a divided by b using the modulo operator
# TODO: Calculate a to the power of b using the exponentiation operator

a = 10
b = 5
# print( a+b, a-b, a/b, a*b)
reste = a % b
# print("Reste (modulo):", reste)
puissance = a ** b
# print("Puissance:", puissance)

# TODO: Create two string variables 'first_name' and 'last_name'
# TODO: Concatenate the two names to create a 'full_name' variable
# TODO: Print the full name in uppercase
# TODO: Print the length of the full name
# TODO: Create a string with multiple words and split it into a list

first_name = "Kevin "
last_name = "Assombi"
full_name = first_name + last_name
# print(full_name)
# print(full_name.upper())
# print(len(full_name))

nba_teams = "Warriors Bulls Nets Lakers"
teams = nba_teams.split()
# print("list of teams:", teams)

# TODO: Convert a string containing a number to an integer
# TODO: Convert a float to an integer
# TODO: Convert an integer to a float
# TODO: Convert a number (integer or float) to a string
# Print all converted values and their new types

strnum = "42"
strnum1 = int(strnum)

floatnum = 3.99
floatnum1 = int(floatnum)

intnum = 7
intnum1 = float(intnum)

num = 12.2
num1 = str(num)

# print(strnum1, type(strnum1))
# print("fl->int:", floatnum1, type(floatnum1))
# print("int->fl:", intnum1, type(intnum1))
# print("num->str:", num1, type(num1))

# TODO: Create two boolean variables
# TODO: Perform AND, OR, and NOT operations on these variables
# Print the results
# TODO: Create two numeric variables and use comparison operators
# (>, <, >=, <=, ==, !=) to compare them
# Print the results of these comparisons

T = True
F = False
# print("and:", T and F)
# print("or: ", T or F)
# print("not:", not F)

x = 2
y = 1

print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
print("x == y:", x == y)
print("x != y:", x != y)