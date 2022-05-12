"""1 створити контекст менеджер, якому можна передати ім'я файла і вміст. На вході він його створить з вмістом"""


class context_manager:
    def __init__(self,name,metod,write):
        self.name = name
        self.metod = metod
        self.write = write

    def __enter__(self):
        self.file = open(self.name,self.metod)
        self.file.write(self.write)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

c_m = context_manager("file.31.txt","a","hello")
print(c_m.__enter__())


