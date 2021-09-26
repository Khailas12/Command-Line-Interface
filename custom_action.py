import argparse


# The nargs (No. of arguments) accepts a couple of extra special parameters. 
# If you want the argument to accept all of the parameters, you can use * which will return all parameters if present, 
# or empty list if none. Positional arguments are determined by the position specified.

class verboseStore(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        
        if nargs is not None:
            raise ValueError('nargs not allowed')
        super(verboseStore, self).__init__(option_strings, dest, **kwargs)
        # super keyword in line ​10 allows the child class to access the parent class's init() property. 
        # In other words, super() allows you to build classes that easily extend the functionality of previously built classes without implementing their functionality again.
        
        
    # The __call__ method enables Python programmers to write classes 
    # where the instances behave like functions and can be called like a function.
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