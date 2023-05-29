import random

def generatePassword(n):
    choice = "<>?abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    password = ""

    for i in range(n):
        password += random.choice(choice)

    return password


if __name__ == "__main__":
    n = int(input("Enter the number:- "))
    password = generatePassword(n)
    print(" Randomly Password:- ", password)
