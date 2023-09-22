
import re
import csv
import getpass
from user import User



#*****************************************************************************************
def check_name_validation(name):
    return True if name.isalpha() else  False


def check_email_exist(email):
    with open('users.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['email'] == email:
                return True
        return False

def check_email_validation(email):
        if len(email) > 7:
            if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email) is not None:
                return True
        
        return False

def check_password_match(password,confirm_password):
    return True if password == confirm_password else False

def check_phone_validation(phone):
    if len(phone) > 10:
        if re.match("^01[0125][0-9]{8}$", phone) is not None:
            # if re.match("r'^(?:\+?44)?[07]\d{9,13}$'", phoneNumber) is not None:
            return True
        return False

while True:
    print(f"===============================")
    print(f"**Crowd Funding App**")
    print("================================")
    print("1. Create a new account")
    print("2. Login")
    print("3. Exit")
    usre_choice = int(input(f"> your choice: "))

    
    if usre_choice == 1:
        print(f"===============================")
        print(f"**New account**")
        print("================================")
        print('**ENTER YOUR DATA**')
        while True:
            first_name = input(f"> Enter your first name: ")
            if not check_name_validation(first_name):
                print('> PLEASE ENTER A VALID NAME.')
                continue
            break    
        while True:
            last_name = input(f"> Enter your last name: ")
            if not check_name_validation(last_name):
                print('> PLEASE ENTER A VALID NAME.')
                continue
            break    
        while True:
            email = input(f"> Enter your email: ")
            if not check_email_validation(email):
                print('> PLEASE ENTER A VALID EMAIL.')
                continue
            if check_email_exist(email):
                print('> Email already exist - Please Enter another one.')
                continue
            break

        while True:
            password = getpass.getpass(prompt=f"> Enter your password: ",)
            if len(password) < 5:
                print('> PLEASE ENTER PASSWORD GREATER THEN 8 DIGITS.')
                continue
            break    
        while True:
            confirm_password = getpass.getpass(prompt=f"> Confirm your password: ")
            if not check_password_match(password,confirm_password):
                print('> PASSWORD DOSN\'T MATCH')
                continue
            break
        while True:
            phone = input(f"> Enter your phone: ")
            if not check_phone_validation(phone):
                print('> PLEASE ENTER A VALID EGP PHONE NUMBER')
                continue
            break    
            
        
        
        user = User(first_name, last_name, email, password,phone)
        user.save_user()
        print(f"=====================================")
        print(f"**Account created successfully**")
        print(f"=====================================")

        

    elif usre_choice == 3:
        print(f"**Exiting**")
        break

    else:
        print(f"**Invalid choice**")
        continue

    
