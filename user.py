import csv

class User:

    def __init__(self, first_name, last_name, email, password,phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        # self.confirm_password = confirm_password
        self.phone = phone
        
    def save_user(self):
        '''
        save_user method saves user object into user_list
        '''
        try:
            with open('users.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=list(self.__dict__.keys()))
                writer.writerow(self.__dict__)
        except IOError:
            print("I/O error")

    
    
    

    