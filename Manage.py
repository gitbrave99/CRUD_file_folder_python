import os
import shutil
from colorama import Fore


class Managef:
    def __init__(self) -> None:
        pass

    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name

    @property
    def pathok(self):
        return self._pathok

    @pathok.setter
    def pathok(self, pathok):
        self._pathok = pathok

    def create_folder(self):
        if os.path.isdir(self._file_name) == True:
            print(Fore.GREEN,f'Folder: {self._file_name} is already created')
        else:
            os.makedirs(self._file_name)
            print(f'Folder: {self._file_name} successfully created')

    def create_textfile(self,textcontent):
        with open(f'{self._file_name}.txt',"w") as file:
            file.write(textcontent)
        print(Fore.GREEN,"All added")

    def show_folders(self):
        with os.scandir(self._pathok) as folders:
            folders = [folder for folder in folders if folder.is_dir()]
        print(folders)

    def show_files(self):
        with os.scandir(self._pathok) as files:
            files = [file for file in files if file.is_file()]
        print(Fore.CYAN,files)
    
    def showFilesFolders(self):
        with os.scandir(self._pathok) as allff:
            allff =[item for item in allff]
        print(Fore.CYAN,allff)

    def delete_folder(self):
        filefolder = self._file_name
        if os.path.exists(filefolder) == True:
            shutil.rmtree(filefolder)
            print(Fore.GREEN, f'folder: {filefolder} has been deleted')
        else:
            print(Fore.RED, f'folder: {filefolder} does not exist')
    def delete_files(self):
        if os.path.exists(self._file_name) == True:
            os.remove(self._file_name)
            print(Fore.GREEN, f'folder: {self._file_name} has been deleted')
        else:
            print(Fore.RED, f'folder: {self._file_name} does not exist')


    def update_folder_file(self, newName):
        if os.path.exists(self._file_name):
            os.rename(self._file_name, newName)
            print(Fore.GREEN, f'Folder:  {self._file_name} has changed to : {newName}')
        else:
            print(Fore.RED, f'{self._file_name} does not exist')
            
