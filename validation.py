import re
import csv
import datetime

class Validation_class:
    
    def check_name_validation(self,name):
        return True if name.isalpha() else  False

    def check_email_validation(self,email):
        if len(email) > 7:
            if re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", email) is not None:
                return True
        
        return False

    def check_password_match(self,password,confirm_password):
        return True if password == confirm_password else False


    def check_phone_validation(self,phone):
        if len(phone) > 10:
            if re.match("^01[0125][0-9]{8}$", phone) is not None:
                return True
            return False


    def check_user(self,email,password):
        
        #Method that checks if a user exists with that email and password and return a Boolean
        
        with open('users.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['email'] == email and row['password'] == password:
                    return True
        return False 


    def check_email_exist(self,email):
        with open('users.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['email'] == email:
                    return True
            return False

#*******************************************************************

    def check_title(self,project_title):
        if len(project_title) > 5 and project_title[0].isalpha():
            return True
        else:
            return False

    def check_date(self,start_date , end_date):
        #today = datetime.date.today().strftime("%Y-%m-%d")
        start_time = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_time = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if start_time > end_time:
            return False
        elif start_time <= end_time:
            return True