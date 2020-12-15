import os 
import numpy as np 
from tqdm.auto import tqdm, trange
from time import sleep 

def read_file(name):
    f = open(name)
    input = f.read().splitlines()
    
    return input


def count_trees(input, right, down, n_sleep=None):
    count = j = 0

    for l in (t := trange(len(input)-down)):
        cursor = j+right
        line = input[l+down]

        rep = None
        if cursor >= len(line):
            rep = np.ceil(cursor / len(line))
            line *= int(rep)+50
        
        if n_sleep is not None: 
            sleep(n_sleep)

        m = line[cursor]
        
        if m == '#':
            count += 1
        
        j += right

        t.set_description(f'Line {l+1}, cursor {cursor}, rep {rep}, found {m}')
         
    return count

