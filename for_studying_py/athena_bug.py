# Demonstrate order of flow intentional bug

name = 'Athena'
age = 2723
if name == 'Genie':
    print('Hi, Genie')
elif age > 80:
    print('You are not Genie, mamaw.')
elif age < 12:
    print('You are not Genie young grasshopper.')
elif age > 2000:
    print('Unlike you, Genie is not an immortal goddess.')

# We were expecting 'Unlike you, Genie is not an immortal goddess
# However, since age is still > then 80 the 
# 'you are not genie, mamaw' statement ran

# The order matters.
