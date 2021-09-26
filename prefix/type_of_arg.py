import argparse


parser = argparse.ArgumentParser()

parser.add_argument(
    '-a',
    action='store',
    type=int
)
# the default type is str but we've assigned int instead

args = parser.parse_args()
print(vars(args))


# I/O -> python type_of_arg.py -a 42
# O/P -> {'a': 42}


# if we provide a string instead
# I/O -> python type_of_arg.py -a "blah blah"
# O/P
# usage: type_of_arg.py [-h] [-a A]
#type_of_arg.py: error: argument -a: invalid int value: 'blah blah'