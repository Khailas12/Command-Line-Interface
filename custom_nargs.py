import argparse

# The nargs (No. of arguments) accepts a couple of extra special parameters. 
# or empty list if none. Positional arguments are determined by the position specified.

parser = argparse.ArgumentParser()

parser.add_argument(
    '--input',
    action='store',
    type=int, 
    nargs=3
)

args = parser.parse_args()
print(args)


# I/O ->  python custom_nargs.py --input 43
# O/P
# usage: custom_nargs.py [-h] [--input INPUT INPUT INPUT]
# custom_nargs.py: error: argument --input: expected 3 arguments


# adding 3 aruments
# I/O -> python custom_nargs.py --input 43 44 45
# O/P
# Namespace(input=[43, 44, 45])