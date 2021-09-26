import argparse



parser = argparse.ArgumentParser()
parser.version = '1.0'

parser.add_argument('-a',action='store')

parser.add_argument('-b',
    action='store_const', 
    const=42
)   # 42 is just a random integer provided


parser.add_argument('-c', action='store_true')
# The store_true action stores a True Boolean when the argument is passed and store a False Boolean elsewhere. If you need the opposite behavior, just use the store_false action:

parser.add_argument('-d', action='store_false')

parser.add_argument('-e', action='append')

parser.add_argument(
    '-f',
    action='append_const',
    const=42
    )

parser.add_argument('-g', action='count')

parser.add_argument('-i', action='help')

parser.add_argument('-j', action='version')


args = parser.parse_args()
print(vars(args))



# on terminal

# I/O -> python action_test.py 
# O/P
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}


# I/O -> python action_test.py "test"
# O/P
# usage: action_test.py [-h] [-a A] [-b] [-c] [-d] [-e E] [-f]
#                       [-g] [-i] [-j]
# action_test.py: error: unrecognized arguments: test


# I/O -> python action_test.py -b
# O/P
# {'a': None, 'b': 42, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}


# I/O -> python action_test.py -e me -e you -e us
# O/P
# {'a': None, 'b': None, 'c': False, 'd': True, 'e': ['me', 'you', 'us'], 'f': None, 'g': None}