import os
from Manage import Managef as Mgf
from colorama import Fore

admin = Mgf()
file_name = ""
option = 100
admin._pathok = os.getcwd()

os.system("cls")
while option != 0:
    print("WELCOME!".center(50, "-"))
    print("1-Create folders \n2-Create files \n3-Delete folders \n4-Delete files" +
          "\n5-Rename folders and files \n6-Print folders\n7-Print files\n8-Print files and folders\n0-End")
    option = int(input("option ->"))
    if option == 1:
        os.system("cls")
        print("CREATE FOLDER!".center(50, "-"))
        file_name = input("Write the filename -> ")
        admin.file_name = file_name
        admin.create_folder()
        input("Enter to main menu...........")
    elif option == 2:
        print("CREATE FILES!".center(50, "-"))
        file_name = input("Write the filename -> ")
        admin.file_name = file_name
        textcontent = input("Write the text content -> ")
        admin.create_textfile(textcontent)
        input("Enter to main menu...........")
    elif option == 3:
        print("DELETE FOLDER!".center(50, "-"))
        file_name = input("Write the filename -> ")
        admin.file_name = file_name
        admin.delete_folder()
        input("Enter to main menu...........")
    elif option == 4:
        print("DELETE FILES!".center(50, "-"))
        file_name = input("Write the filename -> ")
        admin.file_name = file_name
        admin.delete_files()
        input("Enter to main menu...........")
    elif option == 5:
        print("RENAME FOLDER".center(50, "-"))
        file_name = input("Write the file name")
        admin._file_name = file_name
        newName = input("Write the new name")
        admin.update_folder_file(newName)
        input("Enter to main menu...........")
    elif option == 6:
        print("PRINT FOLDERS".center(50, "-"))
        admin.show_folders()
        input("Enter to main menu...........")
    elif option == 7:
        print("PRINT FILES".center(50, "-"))
        admin.show_files()
        input("Enter to main menu...........")
    elif option == 8:
        print("PRINT FOLDERS AND FILES".center(50, "-"))
        admin.showFilesFolders()
        input("Enter to main menu...........")
    elif option == 9:
        print("HAPPY DAY!".center(50, "-"))
        option = 0
        input("Enter to main menu...........")
