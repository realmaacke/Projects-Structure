import os
import shutil
import src.languages as storedLangs

class Project:

    langList = storedLangs.langList
    currentLang = None

    def __init__(self, title, lang, main, path):
        self.title = title
        self.lang = lang
        self.main = main
        self.path = path

        for index in range(len(self.langList)):
            if self.lang == self.langList[index]['name']:
                self.currentLang = self.langList[index]
            
        self.BuildMainFolder()

        if self.main == True:
           
            if 'src' in self.currentLang['folders']:
                mainPath = os.path.join(self.path, "src")
                shutil.copy(self.currentLang['main'], mainPath)

    def BuildMainFolder(self):
        path = os.path.join(self.path, self.currentLang['name'])
        self.path = path
        os.mkdir(path, 0o777)
                
        for index in (self.currentLang['folders']):
            path = os.path.join(self.path, index)
            os.mkdir(path, 0o777)

