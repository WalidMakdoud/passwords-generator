#THis script its my 2nd project for generatore paswword : By : https://github.com/WalidMakdoud
import time
import random
H04x = r"""
██╗░░██╗░█████╗░░░██╗██╗██╗░░██╗
██║░░██║██╔══██╗░██╔╝██║╚██╗██╔╝
███████║██║░░██║██╔╝░██║░╚███╔╝░
██╔══██║██║░░██║███████║░██╔██╗░
██║░░██║╚█████╔╝╚════██║██╔╝╚██╗
╚═╝░░╚═╝░╚════╝░░░░░░╚═╝╚═╝░░╚═╝  https://instagram.com/xx_xwalidxx"""
print(H04X)
while True:
    decision = input("Do you want to generate a password put (Y or n or exit): ")
    if decision == "Y":
        length = int(input("Enter the length of password : "))
        print("Generating Password........")
        s = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+=<>?.,}{[]/-"
        p = ' '
        for i in range(0, length, 1):
            p += s[random.randint(0, len(s))]
        time.sleep(3)
        print(p)
    elif decision == "n":
        print("Thanks for using")
    elif decision == "exit" :
        break
    else :
        print("ERROR")
