import os
import shutil

class MoveToFolder:
    def __init__(self, path = "newfolders",categories = None):
        self.path = path
        self.categories = categories
        self.log = []
    
    def createFolder(self):
        if self.categories:
            for category in self.categories:
                folder = os.path.join(self.path, category)
                try:
                    os.makedirs(folder,exist_ok=True)
                    self._note(f"Создана новая папка: {folder}")
                except OSError as error:
                    self._note(f"Ошибка {error} при создании папки: {folder}")
        else:
            self._note("Списк categories пуст")
    
    def _checkRightName(self,folder,filename):
        if os.path.exists(os.path.join(folder,filename)):
            firstname,lastPart = os.path.splitext(filename)
            k = 1
            while os.path.exists(os.path.join(folder,f"{firstname}{k}{lastPart}")):
                k+=1
            newName = f"{firstname}{k}{lastPart}"
            self._note(f"Файло с таким именем уже был добавлен, поэтому он был переименован в {newName}")
            return os.path.join(folder,newName)
        return os.path.join(folder,filename)

    def moveToFolder(self,email,path,category):
        if os.path.exists(os.path.join(self.path,category)):
            final_path = self._checkRightName(os.path.join(self.path,category),email.filename)
            try:
                shutil.move(os.path.join(path,email.filename),final_path)
                self._note(f"Перемещен новый файл {email.filename} в папку {category}")
            except OSError as error:
                self._note(f"Ошибка при переносе файлa {email.filename}")
        else:
            self._note(f"Папка не существует")

    def _note(self, message):
        self.log.append(message)






        