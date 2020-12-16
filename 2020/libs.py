import os 
import numpy as np 
from tqdm.auto import tqdm, trange
from time import sleep 
from termcolor import colored

def read_file(name):
    f = open(name)
    input = f.read().splitlines()
    
    return input


def count_trees(input, right, down):
    lenght_map = len(input)
    total_move = (lenght_map // down + 1) * right
    lenght_line = len(input[0])

    extention = int(np.ceil(total_move / lenght_line))

    count = j = 0

    for line in (t:= trange(down, len(input), down)):
        cursor = j + right

        raw = input[line]
        
        # extend line
        raw *= extention
       
        m = raw[cursor]

        if m == '#':
            count +=1

        j += right
        
        #sleep(8)
        t.set_description(f'Ext {extention}. Down {line}, right  {cursor}, found {m}')

    return count


def parse_passports(passpts):

    pass_list, pass_temp, out  = [], [], []

    for p in passpts:
        if len(p) == 0:
            pass_list.append(pass_temp)
            pass_temp = []
            continue
        else:
            pass_temp.append(p)
            
   
    for l in pass_list:
        out_dic = {}
        for p in l:
            fields = p.split(' ')
            for f in fields:
                t = f.split(':')
                out_dic[t[0]] = t[1]
        
        out.append(out_dic)
        

    return out


def validate_passports(pass_list, valid_fieds):
    pass






