import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)

parser.add_argument(
    '-v', 
    '--verbose',
    action='store_true',
)

parser.add_argument(
    '--s',
    '--silent',
    action='store_true'
)

args = parser.parse_args()
print(vars(args))

# mutually exclusive grp for options that cannot coexist in the same command line



#  python groups.py -h
# usage: groups.py [-h] (-v | -s)

# optional arguments:
#   -h, --help     show this help message and exit
#   -v, --verbose
#   -s, --silent


# $ python groups.py -v -s
# usage: groups.py [-h] (-v | -s)
# groups.py: error: argument -s/--silent: not allowed with argument -v/--verbose