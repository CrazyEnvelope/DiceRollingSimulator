import tkinter as tk
from tkinter import ttk
import customtkinter
import random
import json

presentPlayers = []

class EnterPlayers(tk.Tk):
    def __init__(self):
        super().__init__()

        #reading data from json
        with open('playerdata.json','r') as file:
            playerData = json.load(file)

        #window setup
        widthW, heightW = (400, 300)
        self.title('Enter Players')
        self.geometry('200x300')
        self.maxsize(widthW, heightW)
        self.minsize(widthW, heightW)
        self.configure(background='#2b2b2a')
        self.resizable(0, 0)

        #info screen
        labelInfo = tk.Label(self, text = "Note! Add user by entering their's name in the filed below,\n or select them from the existing database!", font = ("Helvetica",10),background="#2b2b2a", foreground="white")
        labelInfo.place(relx=0.1,rely=0.1,anchor = tk.NW)

        #combobox setup
        playersFromFile = []
        for player in playerData:
            playersFromFile.append(player["playername"])
        combobox = ttk.Combobox(self,values=playersFromFile)
        combobox.config(width=30)
        combobox.set("Select an existing user")
        combobox.place(relx=0.1,rely=0.49)

        # textbox setup
        textbox = tk.Text(self, height=1, width=25)
        textbox.place(relx=0.1, rely=0.3,anchor = tk.NW)

        #button to add user
        addUserButton = tk.Button(self, text="Add user", font=("Helvetica",10))
        addUserButton.place(relx=0.9,rely=0.29, anchor = tk.NE)

