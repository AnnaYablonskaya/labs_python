import math
import random
from typing import List, Tuple


def preprocess(input: List[int]) -> Tuple[List[int], int]:
    n = len(input)
    blk_idx = -1  # block pointer
    blk_sz = int(math.sqrt(n))  # size of block
    block = []  # decomposed array
    for i in range(n):
        if i % blk_sz == 0:
            blk_idx += 1  # entering next block   
            if len(block) < blk_idx + 1:
                block.append(0)
        block[blk_idx] += input[i]
    return block, blk_sz


def sqrt_decomposition(input: List[int], block: List[int], l: int, r: int, blk_sz: int) -> int:
    assert l > 0
    assert r > 0
    assert r - l >= 0
    assert r < len(input)
    sum_ = 0
    while l < r and l % blk_sz != 0 and l != 0:  #passing the first block
        sum_ += input[l]
        l += 1

    while l + blk_sz <= r:  # passing completely overlapped blocks
        sum_ += block[l // blk_sz]
        l += blk_sz

    while l <= r:  # passing the last block
        sum_ += input[l]
        l += 1

    return sum_


def _test():
    input_ = [i for i in range(1000)]
    random.shuffle(input_)
    l = random.randrange(0, 101)
    r = l + random.randrange(0, 101)
    block, blk_size = preprocess(input_)
    s = sqrt_decomposition(input_, block, l, r, blk_size)
    assert s == sum(input_[l:r + 1])


if __name__ == '__main__':
    num_array = list()
    array_len = input("Enter the amount of elements: ")
    for i in range(int(array_len)):
        n = input("num[{}]: ".format(i))
        num_array.append(int(n))

    l = int(input("Enter left: "))
    r = int(input("Enter right: "))
    block, blk_size = preprocess(num_array)
    s = sqrt_decomposition(num_array, block, l, r, blk_size)
    print("Sum: ", s)
