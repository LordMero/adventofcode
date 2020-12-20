#! /usr/local/bin/python3 

from libs import read_file, parse_passports, validate_passports

valid_fields = ['byr', 'iyr', 'eyr'  'hgt', 'hcl', 'ecl', 'pid', 'cid']

if __name__ == '__main__':

    #passports = read_file('day4input')
    passports = read_file('day4testfile')

    pass_list = parse_passports(passports)

    valid, counter = validate_passports(pass_list, valid_fields)

    print(len(valid) + len(counter))
