import tkinter as tk
from tkinter import ttk
import customtkinter
import random
import json

presentPlayers = []

class EnterPlayers(tk.Tk):
    def __init__(self):
        super().__init__()

        #window setup
        widthW, heightW = (400, 300)
        self.title('Enter Players')
        self.geometry('200x300')
        self.maxsize(widthW, heightW)
        self.minsize(widthW, heightW)
        self.configure(background='#2b2b2a')
        self.resizable(0, 0)

        #info screen
        self.labelInfo = tk.Label(self, text = "Note! Add user by entering their's name in the filed below!\n The database will be erased each time of playing.", font = ("Helvetica",10),background="#2b2b2a", foreground="white")
        self.labelInfo.place(relx=0.1,rely=0.1,anchor = tk.NW)

        #combobox setup
        global presentPlayers
        self.combobox = ttk.Combobox(self,values=presentPlayers)
        self.combobox.config(width=30)
        self.combobox.set("Users added can be seen here!")
        self.combobox.place(relx=0.1,rely=0.49)

        # textbox setup
        self.textbox = tk.Text(self, height=1, width=25)
        self.textbox.place(relx=0.1, rely=0.3,anchor = tk.NW)

        #button to add user
        self.addUserButton = tk.Button(self, text="Add user", font=("Helvetica",10))
        self.addUserButton.place(relx=0.9,rely=0.29, anchor = tk.NE)

        # button to start the game
        self.startButton = tk.Button(self, text="Start", font=("Helvetica", 10))
        self.startButton.place(relx=0.9, rely=0.48, anchor=tk.NE)
        self.startButton.config(width=6)


    def enterPlayers(self):
        global presentPlayers
        playerFromTextBox = self.textbox.get(1.0,"end-1c")
        presentPlayers.append(playerFromTextBox)
        self.combobox.configure(values=presentPlayers)

        presentPlayersDict = []
        for player in presentPlayers:
            presentPlayersDict.append(
                {
                    "rank": 0,
                    "playername": player,
                    "totalscore": 0,
                    "rolls": 0,
                    "lastplayed": "2000-01-01 00:00"
                }
            )

        with open('playerdata.json', 'w') as file:
            json.dump(presentPlayersDict,file,indent=4)



