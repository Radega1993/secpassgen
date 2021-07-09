#!/usr/bin/python

# Include standard modules
import argparse
import sys
import random

def main():
    
    # Initiate the parser
    parser = argparse.ArgumentParser(description="Generate a secure password")
    valid_lenth = ['12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32']
    special_char = ['!','#','$','%','&','(',')','*','+',',','-','.','/','@','[',']','_']
    valid = ['!','#','$','%','&','(',')','*','+',',','-','.','/','@','[',']','_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    
    # Add long and short argument
    parser.add_argument("--len", "-l", choices=valid_lenth, default='12', help="Set the length of the password (12 - 32)")
    args = parser.parse_args()
    leng = args.len
    
    possible_pass = gen_passwd(leng, valid)
    check = check_policy(possible_pass, special_char)
    if check == True:
        final_pass = possible_pass
        print('Your secure password is ---->  ' + final_pass)
        return None
    else:
        main()

def gen_passwd(leng: str, valid: list):
    possible_pass = ''
    last_val = ''
    generating = ''
    for i in range(int(leng)):
        new_val = random.choice(valid)
        if last_val != new_val:
            last_val = new_val
        else:
            new_val = random.choice(valid)
        
        possible_pass = possible_pass + new_val

    return possible_pass

def check_policy(possible_pass: str, special_char: list):
    if check_lower(possible_pass) == True and check_upper(possible_pass) == True and check_number(possible_pass) == True and check_special(possible_pass, special_char) == True: 
        return True
    else:
        return False

def check_lower(possible_pass: str):
    i = 0
    while i < len(possible_pass):
        if possible_pass[i].islower() == True:
            return True
        if i == len(possible_pass):
            return False
        i += 1

def check_upper(possible_pass: str):
    i = 0
    while i < len(possible_pass):
        if possible_pass[i].isupper() == True:
            return True
        if i == len(possible_pass):
            return False
        i += 1

def check_number(possible_pass: str):
    i = 0
    while i < len(possible_pass):
        if possible_pass[i].isdigit() == True:
            return True
        if i == len(possible_pass):
            return False
        i += 1

def check_special(possible_pass: str, special_char: list):
    i = 0
    while i < len(possible_pass):
        if possible_pass[i] in special_char:
            return True
        if i == len(possible_pass):
            return False
        i += 1




if __name__ == "__main__":
    main()
