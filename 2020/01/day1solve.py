from itertools import combinations
from tqdm import tqdm
import numpy as np

def read_file():
    f = open('day1input')
    input = f.read().splitlines()
    input = [int(x) for x in input]
    return input


def find_combo(combo, n_combs, input):
    for i in tqdm(combinations(input, n_combs)):
        s = np.array(i).sum()
        if s == combo:
            return np.array(i), s, np.array(i).prod()


if __name__ == '__main__':
    input = read_file()
    
    find_combo(2020, 3, input)
