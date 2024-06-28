import os
import subprocess



while True:
    print("Please choose a directory: ")
    while True:
        choice = input()
        if os.path.exists(choice):
            print(choice)
            break
        else:
            print("Incorrect Path")

    list = os.listdir(choice)
    print(list)

    while True:
        print("Do you want start intallation? (y/n)")
        user_ipnut =  input().lower().strip()
        if user_ipnut == 'y':
            for i in list:
                subprocess.call(choice + '/' + i, shell=True)
            break
        if user_ipnut == 'n':
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'")

    print("Installation is completely done!!!")






