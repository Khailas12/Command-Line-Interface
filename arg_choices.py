import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '-a',
    action='store',
    choices=['head', 'tail']
)

parser.add_argument(
    '-b',
    action='store',
    choices=range(1, 4)
)
# range is used for numeric values

args = parser.parse_args()
print(vars(args))



# I/O -> python arg_choices.py -b 4
# O/P -> {'a': 4}

# I/O -> python arg_choices.py -b 40    
# O/P
# usage: arg.py [-h] [-a {1,2,3,4}]
# arg_choices.py: error: argument -a: invalid choice: 40 (choose from 1, 2, 3, 4)
# ended up with error because of the number is outta range defined prior