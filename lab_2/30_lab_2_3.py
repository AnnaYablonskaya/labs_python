import os
from tempfile import gettempdir
from itertools import islice, cycle
from collections import namedtuple
import heapq
from progress.bar import Bar
import argparse


Keyed = namedtuple("Keyed", ["key", "obj"])


def merge(key=None, *iterables):
   

    if key is None:
        for element in heapq.merge(*iterables):
            yield element
    else:
        keyed_iterables = [(Keyed(key(obj), obj) for obj in iterable)
                           for iterable in iterables]
        for element in heapq.merge(*keyed_iterables):
            yield element.obj


def batch_sort(input, output, key=None, buffer_size=32000):
    tempdir = gettempdir()

    chunks = []
    try:
        with open(input, 'rb', 64 * 1024) as input_file:
            input_iterator = iter(input_file)

            current_chunk = list(islice(input_iterator, buffer_size))
            if current_chunk:
                current_chunk.sort(key=key)
                output_chunk = open(os.path.join(tempdir, '%06i' % len(chunks)), 'w+b', 64 * 1024)
                chunks.append(output_chunk)
                output_chunk.writelines(current_chunk)
                output_chunk.flush()
                output_chunk.seek(0)   
        with open(output, 'wb', 64 * 1024) as output_file:
            output_file.writelines(merge(key, *chunks))
    finally:
        bar = Bar('Processing', max = buffer_size)  
        for chunk in chunks:
            try:
                chunk.close()
                os.remove(chunk.name)
            except Exception:
                pass
            bar.next()
        bar.finish()

if __name__ == '__main__':
    file_name = input('Enter a filename: ')
    batch_sort(file_name, "{}.sorted".format(file_name))
    parser = argparse.ArgumentParser(description='Input file name')
    parser.add_argument('-a',  
        help='Your file')
    args = parser.parse_args()
    try:
        if args.f:
            file = args.f
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("File does not exists")
    
    
    
       
