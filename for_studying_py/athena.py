# Demonstrating elif statements
# When you want many possible clauses to execute
# You use "else if" statements

name = 'Athena'
age = 2723
if name == 'Genie':
    print('Hi, Genie')
elif age < 12:
    print('You are not Genie young grasshopper.')
elif age > 2000:
    print('Unlike you, Genie is not an immortal goddess.')
elif (age > 76) and (age < 100):
    print('You are not Genie, mamaw.')