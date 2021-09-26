import argparse



parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    action='store',
    default='42'
)   
# setting a defualt value if not provided

args = parser.parse_args()
print(vars(args))

# -a is set to 42, even if the user didn't explicitly set the value on the command line


# I/O -> python default_value.py
# I/P -> {'a': '42'}