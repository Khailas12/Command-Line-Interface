import argparse

# The nargs (No. of arguments) accepts a couple of extra special parameters. 
# or empty list if none. Positional arguments are determined by the position specified.

parser = argparse.ArgumentParser()

parser.add_argument(
    '--input',
    action='store',
    type=int, 
    nargs=3
)   # we have assigned 3 args to be executed in here
# adding 3 aruments
# I/O -> python custom_nargs.py --input 43 44 45
# O/P
# Namespace(input=[43, 44, 45])


parser.add_argument(
    'input',
    action='store',
    nargs='?',
    default='my default value'
)   # ?: a single value, which can be optional
# I/O -> python custom_nargs.py "my custom value"
# O/P
# Namespace(input='my custom value')


parser.add_argument(
    'input',
    action='store',
    nargs='*',
    default='my default value'
)   # *: a flexible number of values, which will be gathered into a list
# I/O -> python custom_nargs.py me you us
# O/P
# Namespace(input=['you', 'us'])


parser.add_argument(
    'input',
    action='store',
    nargs='+',
    default=''
)   # +: like *, but requiring at least one value
#  python custom_nargs.py me you us
# ['me', 'you', 'us']

# python custom_nargs.py
# usage: custom_nargs.py [-h] input [input ...]
# custom_nargs.py: error: the following arguments are required: input

# argparse.REMAINDER: all the values that are remaining in the command line

parser.add_argument('first', action='store')
parser.add_argument(
    'others', action='store', nargs=argparse
    )

args = parser.parse_args()
print(args)
print('first = %r' % args.first)
print('others = %r', args.others)
# I/O-> python nargs_example.py me you us
# O/P
# first = 'me'
# others = ['you', 'us']


# I/O ->  python custom_nargs.py --input 43
# O/P
# usage: custom_nargs.py [-h] [--input INPUT INPUT INPUT]
# custom_nargs.py: error: argument --input: expected 3 arguments