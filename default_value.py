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