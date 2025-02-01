a = open('log_file_zad8.1.txt', 'r+')


a = a.readlines()

users = []

for i in a:
    if("'" in i):
        x = i.split("'")
        if(not x[1] in users):
            users.append(x[1])

print(users)