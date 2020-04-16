
import os
import sys
import string
import random
from typing import Tuple
from progress.bar import Bar


def random_str_generator(size: int) -> str:
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(size))


def size_of_str_in_bytes(s):  # Encodes a string into bytes 
    return len(s.encode('utf-8'))


def generate_file(file_name: str, size_in_mb: int, l: Tuple[int, int], k: Tuple[int, int]) -> None:
    bytes_written = 0
    bar = Bar('Processing', max = size_in_mb * 1000000)
    with open(file_name, 'w') as f:
        while bytes_written < size_in_mb * 1000000:
            number_of_words = random.randrange(k[0], k[1])
            line = ' '.join([random_str_generator(random.randrange(l[0], l[1])) for _ in range(number_of_words)])
            f.write(line + "\n")
            bytes_written += size_of_str_in_bytes(line)
            bar.next()
        bar.finish()

if __name__ == '__main__':
    k = (10, 100)
    l = (3, 10)
    if len(sys.argv) > 1:
        print(sys.argv)
        fname = sys.argv[1]
        sz_in_mb = int(sys.argv[2])
        if len(sys.argv) == 5:
            k = sys.argv[3]
            l = sys.argv[4]
    else:
        fname = input("File name: ")
        sz_in_mb = int(input("Mb: "))
        k = input("Range of words in line (separated with comma), can be empty: ")
        l = input("Range of symbols in word (separated with comma), can be empty: ")

    if os.path.exists(fname):
        raise Exception("File already exists")

    assert sz_in_mb > 0

    if type(k) is str:
        k = [int(_) for _ in k.split(",")]

    if type(l) is str:
        l = [int(_) for _ in l.split(",")]

    generate_file(fname, sz_in_mb, l, k)
 