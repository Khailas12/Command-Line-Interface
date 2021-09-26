import argparse
import sys
import os


# creating parser
parser = argparse.ArgumentParser(
    prog='myls',
    usage='%(prog)s [options] path',
    description='List the content of a folder',
    epilog='Have a nice day! :)',
    prefix_chars='=',
    add_help=True
    )    
# prog=: name of the program 
# usage=: shows the help info from default
# description=: for the text that is shown before the help text
# epilog=: for the text shown after the help text
# By default, the standard prefix char is the dash (-). eg: -help
# add_help=False -> to disable the help feature and -h wouldn't be accepted
# action -> This specifies to store the value to the Namepsace object when executed. basically it's characteristics 

# adding arguments
parser.add_argument(
    'Path',
    metavar='path',
    type=str,
    help='the path of list'
)



# executing the parse_args() method
args = parser.parse_args()   # Executing the parse.args() method

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()
    
print('\n'.join(os.listdir(input_path)))


# I/O
# python myls.py =h