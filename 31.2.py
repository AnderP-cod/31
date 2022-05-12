"""2 створити контекст менеджер, якому можна передати ім'я папки і назви файлів.
    На вході він створить папку з усіма файлами"""

import os
import shutil

class context_manager:
    def __init__(self,folder,name,metod,write):
        self.folder = folder
        self.name = name
        self.metod = metod
        self.write = write

    def __enter__(self):
        os.makedirs(self.folder)
        self.file = open(self.name,self.metod)
        self.file.write(self.write) 
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

c_m = context_manager("Тридцать один","file.31.2.txt","a","31.2")
print(c_m.__enter__())



