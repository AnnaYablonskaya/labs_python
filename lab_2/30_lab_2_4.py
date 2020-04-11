from collections import Iterable  
import argparse

def flatten_it(items):
    """
    Yield items from any nested iterable;
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten_it(x):
                yield sub_x
        else:
            yield x


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--array', type=float, action='append', 
                        nargs='+', help='array to flatten')
    inputs = parser.parse_args()
    arr = inputs.array
    if arr:
        print(arr) 
        print(list(flatten_it(arr)))
    else:
        print('Enter input arguments')
