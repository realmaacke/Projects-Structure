import customtkinter
import tkinter

import src.structures as src
import src.languages as storedLangs

from tkinter import filedialog

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("system")

class App(customtkinter.CTk):
    main = False
    langList = []

    def __init__(self):
        super().__init__()

        self.geometry("600x500")
        self.title("ProjectInit")


        for index in range(len(storedLangs.langList)):
            self.langList.append(storedLangs.langList[index]['name'])

        self.nameEntry = customtkinter.CTkEntry(self, placeholder_text="Project Name")
        self.nameEntry.pack(padx=10, pady=10)
            
        self.languageButton = customtkinter.CTkComboBox(self,values=self.langList, command=self.language_Callback)
        self.languageButton.pack(padx=10, pady=10)

        self.MainButton = customtkinter.CTkCheckBox(self, text="Generate main file", command=self.checkMain, onvalue=True, offvalue=False)
        self.MainButton.pack(padx=10, pady=10)

        self.PathButton = customtkinter.CTkButton(self,text="path", command=self.OpenFileDialog)
        self.PathButton.pack(padx=10, pady=10)

        self.GenerateButton = customtkinter.CTkButton(self, text="Generate", command=self.Generate)
        self.GenerateButton.pack(padx=10, pady=10)

    def OpenFileDialog(self):
        self.path = filedialog.askdirectory()

    def language_Callback(self, choice):
        self.lang = choice

    def checkMain(self):
       self.main = self.MainButton.get()

    def name_Callback(self):
        self.name = self.nameEntry.get()

    def Generate(self):
        self.project = src.Project(self.nameEntry.get(), self.languageButton.get(), self.main, self.path)
