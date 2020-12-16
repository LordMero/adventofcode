#! /usr/local/bin/python3 

from libs import read_file, parse_passports



if __name__ == '__main__':

    passports = read_file('day4input')

    pass_list = parse_passports(passports)


