import argparse


class verboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(verboseStore, self).__init__(option_strings, dest, **kwargs)
        
    def __call__(self, parser, namespace, values, option_strings=None):
        print(
            'setting the value %r for the %r option!' % (values, option_strings)
        )
        setattr(namespace, self.dest, values)
        

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i',
    '--input',
    action=verboseStore,
    type=int,
)

args = parser.parse_args()
print(args)