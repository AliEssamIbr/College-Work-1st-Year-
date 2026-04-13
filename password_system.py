import random as r
import csv
Cap_let = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Sml_let = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["1","2","3","4","5","6","7","8","9"]
symbols =["@","#","$","%","*","&"]
password = ""
the_list = []
for i in range(100):
    password = ""
    choice = r.randint(0,25)
    temp = Cap_let[choice]
    password+=temp
    for i in range(6):
        big_choice = r.randint(1,4)
        if big_choice == 1:
            choice = r.randint(0,25)
            password += Cap_let[choice]
        elif big_choice == 2:
            choice = r.randint(0,25)
            password += Sml_let[choice]
        elif big_choice == 3:
            choice = r.randint(0,8)
            password += num[choice]
        elif big_choice == 4:
            choice = r.randint(0,5)
            password += symbols[choice]
    if password in the_list:
        print("invalid")
    else:
        the_list.append(password)
print(the_list)
with open("passwords.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["password"])
    for pwd in the_list:
        writer.writerow([pwd])
print("\n100 password generated")

