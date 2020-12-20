import os 
import numpy as np 
import re
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


def validate_passports(pass_list, valid_fields):
        
    v = set(valid_fields)

    valid, counter = [], []
    
    for p in pass_list:
        
        k = set(list(p.keys()))

        if len(v-k) == 0:
            valid.append(p)
        elif v-k == set(['cid']):
            counter.append(p)
    
    return valid, counter


def validate_fields(p, fld):
    v = p[fld]
    if fld == 'byr':
        if int(v) > 1920 and int(v) < 2002:
            return True
    elif fld == 'iyr':
        if int(v) > 2019 and int(v) < 2020:
            return True
    elif fld == 'eyr':
        if  len(v) == 4 and int(v) > 2020 and int(v) < 2030:
            return True
    elif fld == 'hgt':
        if v.endswith('cm') and int(v.strip('cm')) > 150 and int(v.strip('cm')) < 193:
            return True
        elif v.endswith('in') and int(v.strip('in')) > 59 and int(v.strip('in')) < 76:
            return True
    elif fld == 'hcl':
        if v.startswith('#'):
            if len(re.findall('[0-9a-f]', v)) == 6:
                return True
    elif fld == 'ecl':
        if v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:   
            return True
