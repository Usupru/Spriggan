import pyfiglet
import termcolor
from cryptography.fernet import Fernet
import os
from os.path import isfile
from os import listdir
import time

fileCount = 0

def readKey():
    try:
        return open("key.key", "rb").read()
    except:
        return("Error")



text = pyfiglet.figlet_format("Decrypter")

# Aplica colores
colored_text = termcolor.colored(text, color="magenta", attrs=["bold"])

# Muestra el texto
print(colored_text)

print(termcolor.colored("Welcome to the decrypter", color="magenta"))
input(termcolor.colored("\nPress any key to continue ", color="magenta"))

directory = input(termcolor.colored("\nEnter the main directory to be decrypted (leave blank to use the current one): ", color="yellow"))

if len(directory) > 1:
    directory = directory
else:
    directory = os.getcwd()

key = readKey()

if key == "Error":
    print(termcolor.colored("\nERROR: Key not available, be sure to have the key in the same directory", color="red", attrs=["bold"]))
    quit()

choice = input(termcolor.colored("\nAre you sure you want to continue? y/n ", color="magenta", attrs=["bold"]))

if "y" in choice:
    print(termcolor.colored("\nStarting decryption process \n", color="red", attrs=["bold"]))

    key = readKey()

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file not in ["spriggan.py", "key.key", "decrypt.py"]:

                filePath = os.path.join(root, file)

                contents = open(filePath, "rb").read()
                f = Fernet(key)

                contents = f.decrypt(contents)

                with open(filePath, "wb") as targetFile:
                    targetFile.write(contents)
            
                print(termcolor.colored("Decrypting " + str(file), color="yellow"))

                fileCount = fileCount + 1


    print(termcolor.colored("\nDecryption successful, " + str(fileCount) + " files have been decrypted", color="green", attrs=["bold"]))

else:
    print(termcolor.colored("\nQUITTING! \n", color="red", attrs=["bold"]))
