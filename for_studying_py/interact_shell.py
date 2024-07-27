# Operators for the operation will be listed within parenthesis.

# Below is an expression.
2 + 2 

# Below is an exponent(**) operation.
4 ** 3

# Below is a Modulus/remainder(%) operation.
12 % 10

# Below is the Integer division/floored quotient(//) operation.
40 // 4 

# Below is the Division(/) operation.
32 / 4

# Below is the Multiplication(*) operation.
5 * 5

# Below is the Subtraction(-) operation.
10 - 5

# Below is the Addition(+) operation.
4 + 4

# The order of operations (also called precendence) of python
# math operators is similar to that of mathematics.
# You can use parentheses to override the usual precendence
# if you need to.

# Below is a string concatentation(+ when strings) operation.
'Alice' + 'Bob'

# Below is string replication, when multiply str by int.
'Alice' * 6
# The * operator can be used with only two numeric values
# (for multiplication), or one string value and one integer
# value (for string replication). Otherwise, Python will just
# display an error message.

# You'll store values in variables with an assignment statement.
# An assignment statement consists of a variable name, an 
# equal sign (=) (called the assignment operator), and the value 
# to be stored. If you enter the assignment statement spam = 42,
# then a variable named spam will have the integer value 42 stored
# in it.
spam = 40
spam
eggs = 2
spam + eggs
spam + eggs + spam

spam = 'Hello'
spam

spam = 'Goodbye'
spam

# The str(), int() and float() functions will evaluate 
# to string, integer or float.
# You can take the various data types and change them as needed
# for your program.

str(0)
str(-3.14)

int('42')
int('-99')

int(1.25)
int(1.99)

float('3.14')
float(10)

# The input() function always evaluates to string.
# Even if you are working with numbers.

spam = input() # better way listed below.
spam

# But if you pass the variable spam as an argument.
# in the int() or float() functions. 
# You can convert to integers or floats.

print(f'we cannot add ' + spam + ' '+ spam +' as strings')
print('But we can use int() or float() to convert them for calculation')
print(int(spam) + int(spam))

# A better way would be to cast the value to int rigth on input
spam = int(input())
spam

spam + spam

bacon = 20
bacon + 1
bacon

# round function 

round(10.2, ndigits=None) # Returns 10.2 rounded to an integer

round(10.2) # Also returns 10.2 rounded to an integer 

round(11.2822, 2) # Rounds to 2 decimal places
