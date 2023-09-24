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
        
        
        while True:
            project_disc = input("> Enter Project Your Discription: ")
            if not validation.check_disc(project_disc):
                print("Please Enter a valid Discription")
                continue
            else:
                break

        while True:
            target = input("> Enter Your Target: ")
            if not validation.check_target(target):
                print("Please Enter a valid Target")
                continue
            else:
                break

        while True:
            start_date = input("> Enter Your Start Date: ")
            if not validation.check_start_date(start_date):
                print("Please Enter a valid Start Date")
                continue
            else:
                break
        

        while True:
            end_date = input("> Enter Your End Date: ")
            if not validation.check_end_date(start_date, end_date):
                print("Please Enter a valid End Date")
                continue
            else:
                break
        
        try:
            new_project = Project(user,project_title,project_disc,target,start_date,end_date)
            new_project.save_projects()
            print("=============================")
            print("**Project Created**")
            print("=============================")
        except e:
            print(e)    

    def list_projects(user):
        projects = []
        with open('projects.csv','r') as f:
            reader = csv.DictReader(f)
            i = 1
            print("\n\n\n========List Projects============")
            for row in reader:
                if row['user'] == user:
                    print(f"[{i}] {row['title']}")
                    projects.append(row)
                    i += 1
            print("===============T=================\n\n\n")
            return projects

    def update_project(user,head,old_value,new_value):
        data_list = []    
        with open('projects.csv' , 'r') as file:
            reader = csv.DictReader(file)
            
            
            for row in reader:
                data_list.append(row)
                
            
            for dict in data_list:
                if dict[head] == old_value and dict['user'] == user:
                    dict[head] = new_value
                    print(f"New {head} is: {dict[head]}")
                        
        with open('projects.csv','w') as file:
            writer = csv.DictWriter(file, fieldnames=list(data_list[0].keys()))
            writer.writeheader()
            writer.writerows(data_list)


    def delete_project(user):
        projects=Project.list_projects(user)
        while True:
            project_id = input("> Choose Project ID You want to Delete it 0 to cancel: ")
            if int(project_id) == 0:
                break
            elif project_id.isnumeric() and int(project_id) <= len(projects):
                data_list = []
                title = projects[int(project_id)-1]['title']
                with open('projects.csv' , 'r') as file:
                    reader = csv.DictReader(file)
                    
                    
                    for row in reader:
                        if row['user'] == user and row['title'] == title:
                            continue
                        else:
                            data_list.append(row)

                    # print(data_list)
                with open('projects.csv','w') as file:
                    writer = csv.DictWriter(file, fieldnames=list(projects[0].keys()))
                    writer.writeheader()
                    writer.writerows(data_list)
                break

    def edit_project(user):
        projects=Project.list_projects(user)

        while True:
            project_id = input("> Choose Project ID You want to change it 0 for exit : ")
            if int(project_id) == 0:
                break
            elif project_id.isnumeric() and int(project_id) <= len(projects):
                old_row = projects[int(project_id)-1]
                # print(old_row)
                print("\t========================================")
                print(f"\t\t [1] to change project title.")
                print(f"\t\t [2] to change project description.")
                print(f"\t\t [3] to change project target.")
                print(f"\t\t [4] to change project start date.")
                print(f"\t\t [5] to change project end date.")
                print(f"\t\t [6] to Exit.")
                print("\t========================================")
                
                change_num = input("> Choose Process: ")
                if change_num.isnumeric() and int(change_num) <= 6 and int(change_num) == 1:
                    while True:
                        new_title = input("> Enter New Title: ")
                        if not validation.check_title(new_title):
                            print("Please Enter a valid Title")
                            continue
                        else:
                            try:
                                Project.update_project(user,'title' , projects[int(project_id)-1]['title'] , new_title)
                                Project.edit_project(user)
                            except e:
                                print(e)
                
                elif change_num.isnumeric() and int(change_num) <= 6 and int(change_num) == 2:
                    while True:
                        new_disc = input("> Enter New Discription: ")
                        if not validation.check_disc(new_disc):
                            print("Please Enter a valid Discription")
                            continue
                        else:
                            try:
                                Project.update_project(user,'description' , projects[int(project_id)-1]['description'] , new_disc)
                                Project.edit_project(user)
                            except e:
                                print(e)
                
                elif change_num.isnumeric() and int(change_num) <= 6 and int(change_num) == 3:
                    while True:
                        new_target = input("> Enter New Target: ")
                        if not validation.check_target(new_target):
                            print("Please Enter a valid Target")
                            continue
                        else:
                            try:
                                Project.update_project(user,'target' , projects[int(project_id)-1]['target'] , new_target)
                                Project.edit_project(user)
                            except e:
                                print(e)


                elif change_num.isnumeric() and int(change_num) <= 6 and int(change_num) == 4:
                    while True:
                        new_start_date = input("> Enter New start date: ")
                        if not validation.check_start_date(new_start_date):
                            print("Please Enter a valid Date")
                            continue
                        else:
                            try:
                                Project.update_project(user,'start_date' , projects[int(project_id)-1]['start_date'] , new_start_date)
                                Project.edit_project(user)
                            except e:
                                print(e) 

                elif change_num.isnumeric() and int(change_num) <= 6 and int(change_num) == 5:
                    while True:
                        new_end_date = input("> Enter New End Date: ")
                        if not validation.check_end_date(projects[int(project_id)-1]['start_date'],new_end_date):
                            print("Please Enter a valid Date")
                            continue
                        else:
                            try:
                                Project.update_project(user,'end_date' , projects[int(project_id)-1]['end_date'] , new_end_date)
                                Project.edit_project(user)
                            except e:
                                print(e)            

                elif change_num.isnumeric() and int(change_num) <= 6 and int(change_num) == 6:    
                
                    break

                else:
                    print("Please Enter a valid Process")
                
                break

            else:
                print("Please Enter a valid Project ID")


    
# Project.delete_project('hassan@ahmed.aha')



