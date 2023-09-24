
import re
import os
import datetime
import csv
import getpass
from user import User
from validation import Validation_class
from project import Project



def project_menu(user):
    while True:
        print("[1] Create a new Project")
        print("[2] View the Projects")
        print("[3] Edit Project")
        print("[4] Delete Project")
        print("[5] Exit")
        choice = input("> Enter your choice: ")
        if choice == "1":
            Project.create_project(user)
        elif choice == "2":
            Project.list_projects(user)
        elif choice == "3":
            Project.edit_project(user)
        elif choice == "4":
            Project.delete_project(user)
        elif choice == "5":
            main()
        else:
            print("Please enter a valid choice")
            continue



#*****************************************************************************************


validation = Validation_class()
# project = Project()

def main():
    while True:
        print(f"\t==================================")
        print(f"\t\t**Crowd Funding App**")
        print("\t===================================\n")
        print("[1] Create a new account")
        print("[2] Login")
        print("[3] Exit\n")
        usre_choice = int(input(f"> your choice: "))

        
        if usre_choice == 1:
            print(f"\t===================================")
            print(f"\t\t**New account**")
            print("\t====================================\n")
            print('\t\t**ENTER YOUR DATA**')
            while True:
                first_name = input(f"> Enter your first name: ")
                if not validation.check_name_validation(first_name):
                    print('> PLEASE ENTER A VALID NAME.')
                    continue
                break    
            while True:
                last_name = input(f"> Enter your last name: ")
                if not validation.check_name_validation(last_name):
                    print('> PLEASE ENTER A VALID NAME.')
                    continue
                break    
            while True:
                email = input(f"> Enter your email: ")
                if not validation.check_email_validation(email):
                    print('> PLEASE ENTER A VALID EMAIL.')
                    continue
                if validation.check_email_exist(email):
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
                if not validation.check_password_match(password,confirm_password):
                    print('> PASSWORD DOSN\'T MATCH')
                    continue
                break
            while True:
                phone = input(f"> Enter your phone: ")
                if not validation.check_phone_validation(phone):
                    print('> PLEASE ENTER A VALID EGP PHONE NUMBER')
                    continue
                break    
                
            
            
            user = User(first_name, last_name, email, password,phone)
            user.save_user()
            print(f"\n\n\t==========================================")
            print(f"\t\t**Account created successfully**")
            print(f"\t==========================================\n\n")

            
        elif usre_choice == 2:
            print(f"\n\t=================================")
            print(f"\t\tLogin")
            print(f"\t=================================\n")

            while True:
                login_email= input(f"> Enter Your Email: ")
                login_passowrd= getpass.getpass(prompt=f"> Enter your password: ")
            
                if validation.check_user(login_email,login_passowrd):
                    print(f"\n\t========================================")
                    print(f"\t\t**Login successful**")
                    print(f"\t========================================\n\n")
                    project_menu(login_email)
                    
                else:
                    print(f"\t\t**Invalid credentials**")
                    continue
                
            
        elif usre_choice == 3:
            print(f"\t\t**Exiting**")
            exit()

        else:
            print(f"\t\t**Invalid choice**")
            continue

    
if __name__ == "__main__":
    main()