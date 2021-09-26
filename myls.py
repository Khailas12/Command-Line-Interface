import argparse
import os
import sys


# creating parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')


# adding arguments
my_parser.add_argument(
    'Path',
    metavar='path',
    type=str,
    help='the path of list'
)

args = my_parser.parse_args()   # Executing the parse.args() method

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()
    
print('\n'.join(os.listdir(input_path)))