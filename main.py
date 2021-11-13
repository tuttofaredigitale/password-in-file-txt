import random

def gen_password(lun):
    password = ""
    for i in range(lun):
        password += random.choice("abcdefghijklmnopqrstuvwxyz")
    return password

def gen_password_x(number, lun):
    password = []
    for i in range(number):
        password.append(gen_password(lun))
    return password

def salva_pwd(passwords):
    file = open("passwords.txt", "w")
    for password in passwords:
        file.write(password + "\n")
    file.close()

def main():
    number = int(input("Quante passwords vuoi generare?"))
    lun = int(input("Quanto lunghe devono essere le passwords?"))
    passwords = gen_password_x(number, lun)
    salva_pwd(passwords)
    print("Le passwords sono salvate in passwords.txt")

main()
