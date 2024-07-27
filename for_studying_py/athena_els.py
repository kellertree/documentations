# Testing else statement to run if elif don't run
# Athena program using if, elif, and else clauses.

name = 'Athena'
age = 2723

if name =='Genie':
    print('Hi, Genie.')
elif age < 12:
    print('You are not Genie, young grashopper.')
else:
    print('You are neither Genie nor a young grasshopper.')

# When you use if, elif, and else statements together, remember
# these rules about how to order them to avoid bugs.

# First there is always exactly one if statement.
# Any elif statements you need should follow the if statement.
# Second, if you want to be sure that at least one clause
# is executed, close the structure with an else statement.