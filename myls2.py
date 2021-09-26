import argparse
import sys
import os


parser = argparse.ArgumentParser(
    description='List of content of a folder'
)

parser.add_argument(
    'Path',
    metavar='path',
    type=str,
    help='the path to list'
)

# here adds the opitional arguments. check the notes for detailed info
parser.add_argument(
    '-l',
    '--long',
    type=str,
    help='the path to list'
)


args = parser.parse_args()
input_path = args.path


if not os.path.isdir(input_path):
    print('The path specidied does not exist')
    sys.exit()
    
for line in os.listdir(input_path):
    if args.long:
        size = os.start(os.path.join(input_path, line)).st_size
        lint = '%10d %s' % (size, line)
    print(line)