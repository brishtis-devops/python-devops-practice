import os


# file name to check
filename = input("Enter the file name: ")

if os.path.isfile(filename):
    print("The file exists in the directory.")
else:
    print("The file does not exists in the directory,")
