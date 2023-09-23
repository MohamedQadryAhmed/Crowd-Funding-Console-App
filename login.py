import csv


email = 'ahmed@ali.ss'
password = '147852'
with open('users.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['email'] == email:
            while True:
                password = input('enter password: ')
                if password == row['password']:
                    print('login success')
                    break
                else:
                    print('wrong password')
        else:
            print('wrong email')
        


