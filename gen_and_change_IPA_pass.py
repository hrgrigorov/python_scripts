import random
import os

#####
#This script generate new random password/s and apply it to the IPA user/s from "userlist" file
# and store users and their passwords in "passwords_and_users.csv" file.
# Usage: just populate "userlist" file with the name of the users (one user per line) which
# password should be changed and then run the script. "userlist" file should be located in the
# same location wiht the script file.   
#####

LOWER_LETTERS = [chr(char) for char in range(97,123)]
UPPER_LETTERS = [chr(char) for char in range(65,91)]
NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '%', '@', '&', '*']

def generate_password():
    pass_lowers = [random.choice(LOWER_LETTERS) for _ in range(5)]
    pass_upper = [random.choice(UPPER_LETTERS) for _ in range(1)]
    pass_num = [random.choice(NUMS) for _ in range(1)]
    pass_symbol = [random.choice(SYMBOLS) for _ in range(1)]

    pass_list = pass_lowers + pass_upper + pass_num + pass_symbol
    random.shuffle(pass_list)
    password = ''.join(pass_list)
    return password

with open("userlist") as u:
    users =[user.strip() for user in u.readlines()]
    
for u in users:
    new_pass = generate_password()
    data = "%s,%s" % (u, new_pass)
    with open("passwords_and_users.csv", mode="a") as r:
        r.writelines(data + "\n")
    os.system('echo %s | ipa user-mod %s --password' %(new_pass, u))
