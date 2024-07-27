# Although integer, float and string have infinite data types
# Boolean data types only have two values: True or False
# Below we review Boolean values.

spam = True # sets spam to True

spam

# == equal to operator
# != not equal to operator
# < less than operator
# > greater than operator
# <= less than or equal to operator
# >= greater than or equal to operator

72 == 72 # evaluates to True because 72 = 72.

39 == 72 # evaluates to False because 39 does not equal 72

25 != 32 # evaulates to True because 25 does not equal 32

6 != 6 # evaulates to False because 6 = 6

# The operators evaluate to True or False depending on 
# the values they are given.

# == (equal to) evaluates to True when both sides are same
# != (not equal to) evaluates True when two values are different

# The == and != operators can work with values of any data type

'greetings' == 'greetings' # True because strings are same

'greetings' == 'goodbyes' # False because values differ

'greetings' == 'Greetings' # False because case sensitivity

'dragon' != 'penguin' # True because dragon is not equal to penguin

True == True # evaluates to True because True = True

True != False # evaluates to True because True != False

50 == 50.0 # True because 50 and 50.0 are equivalent

50 == '50' # False because 50 is integer and '50' is string


# The <, >, <=, and >= operators only work properly with 
# integer and floating-point values.

57 > 27

32 < 58

50 < 50

cookie_count = 12
cookie_count <= 12

car_year = 2018
car_year >= 2010

# Boolean operators (and, or, and not) are used to compare Boolean 
# values liek comparison operators. They evaluate these
# expressions down to a Boolean value.

# Binary Boolean Operators
# The and and or operators always take two Boolean 
# values (or expressions), so they're considered binary operators.

# The and operator evaluates an expression to True
# if both Boolean values are True

True and True

True and False

(5 + 5) == 10 and (4+6) == 10

(5 + 5) == 10 and (10 + 10) == 10

(5 + 10) == 10 and (5 + 5) == 10

# The or operator evaluates True if either of the two
# Boolean values is True

(5 + 10) == 10 or (5 + 5) == 10

# If both are false it evaluates to false
(5 + 10) == 12 or (5 + 5) == 12

# The not operator only operates on one Boolean 
# value (or expresion)
# The not operator evaluates to the opposite Boolean value

not True

not not not not True

not False

# Mixing Boolean and Comparison Operators
# Since comparison operators evaluate to Boolean values,
# you can use them in expressions with the Boolean operators.


(4 < 5) and (5 < 6)