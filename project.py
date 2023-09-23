import re
import csv
import datetime
from validation import Validation_class

validation = Validation_class()

class Project:
    

    def __init__(self,user,title,description,target,start_date,end_date):
        self.user = user
        self.title = title
        self.description = description
        self.target = target
        self.start_date = start_date
        self.end_date = end_date

    
    def save_projects(self):
        try:
            with open('projects.csv', 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=list(self.__dict__.keys()))
                writer.writerow(self.__dict__)
        except IOError:
            print("I/O error")

    # def show_projects(self,user):
    #     with open('projects.csv','r') as f:
    #         reader = csv.DictReader()
    #         i = 1
    #         for row in reader:
    #             if row['user'] == user:
    #                 print(f"[{i}] {row['title']}")
    #                 i += 1


    def create_project(user):
        while True:
            project_title = input("> Enter Project Your Title: ")
            if not validation.check_title(project_title):
                print("Please Enter a valid Title")
                continue
            else:
                break
        
        
        project_disc = input("> Enter Project Your Discription: ")

        while True:
            target = input("> Enter Your Target: ")
            if target.isnumeric() and int(target) < 25000:
                break
            else:
                print("Please Enter a valid Target Maximum is $25000")
                continue

        while True:
            start_date = input("> Enter Your Start Date: ")
            today = str(datetime.date.today())
            if re.match(r'^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', start_date) and validation.check_date(today, start_date):
                break
            else:
                print("Please Enter a valid Start Date")
                continue        
        

        while True:
            end_date = input("> Enter Your End Date: ")
            if re.match(r'^[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$', end_date) and validation.check_date(start_date, end_date):
                break
            else:
                print("Please Enter a valid End Date")
                continue
        
        try:
            new_project = Project(user,project_title,project_disc,target,start_date,end_date)
            new_project.save_projects()
            print("=============================")
            print("**Project Created**")
            print("=============================")
        except e:
            print(e)    

    def list_projects(user):
        with open('projects.csv','r') as f:
            reader = csv.DictReader(f)
            i = 1
            print("========List Projects============")
            for row in reader:
                if row['user'] == user:
                    print(f"[{i}] {row['title']}")
                    i += 1
                else:
                    print("No Projects Found!")
            print("===============T=================")


    
