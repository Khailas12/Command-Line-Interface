import argparse


# allow_abbrev -> helps to run on the terminal even if we inputs -in instead of --input . well if it written False, then the abbreviation wouldn't be possible
parser = argparse.ArgumentParser(allow_abbrev=True)    
parser.add_argument(
    '--input', 
    action='store',
    type=int,
    required=True,
)
# action=store -> stores the input value to the Namepsace Obj. This is default action

parser.add_argument(
    '--id',
    action='store',
    type=int
)

args = parser.parse_args()
print(args.input)


# this makes to run it on the terminal with prefix shortned but a single letter input could lead to a trouble.

# I/O
# python abbreviation_test.py --input 42

# O/P
# 42

# I/O
# python abbreviation_test.py --in 42

# O/P
# 42