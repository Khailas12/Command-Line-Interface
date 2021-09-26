import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars='=')

parser.add_argument(
    'a',
    help='first argument'
)

parser.add_argument(
    'b',
    help='second argument'
)

parser.add_argument(
    'c',
    help='third argument'
)

parser.add_argument(
    '--v',
    '--verbose',
    action='store_true',
    help='optional argument'
)


# executing parse_args()
args = parser.parse_args()
print('You have provided all the parameters required to execute')