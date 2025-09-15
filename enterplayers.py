import tkinter as tk
from tkinter import ttk
import customtkinter
import random
import json
import re

presentPlayers = []
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

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
        self.addUserButton = customtkinter.CTkButton(
            self,
            text='Add user',
            border_color='white',
            border_width=1,
            border_spacing=5,
            corner_radius=10,
            font=("Helvetica", 15,'bold'),
            height=20,
            width=50
        )
        self.addUserButton.place(relx=0.9, rely=0.29, anchor=tk.NE)

        # button to start the game
        self.startButton = customtkinter.CTkButton(
            self,
            text='Start',
            border_color='white',
            border_width=1,
            border_spacing=5,
            corner_radius=10,
            font=("Helvetica bold", 15,'bold'),
            height = 20,
            width=50,
            hover_color = "#267b0d",
            fg_color = "#447A09"
        )
        self.startButton.place(relx=0.9, rely=0.49, anchor=tk.NE)

        # Error messages
        self.errorMsg = tk.Label(self,
                                  text="",
                                  font=("Helvetica", 10), background="#2b2b2a", foreground="red")
        self.errorMsg.place(relx=0.1, rely=0.7, anchor=tk.NW)


    def enterPlayers(self):
        global presentPlayers
        playerFromTextBox = self.textbox.get(1.0,"end-1c")

        if regex.search(playerFromTextBox) == None:
           if playerFromTextBox != "":
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
                           "lastplayed": "yyyy-mm-dd"
                       }
                   )

               self.textbox.delete('1.0', tk.END)
               self.errorMsg.config(text='')
               with open('playerdata.json', 'w') as file:
                   json.dump(presentPlayersDict, file, indent=4)
           else:
                self.errorMsg.config(text="Please, insert at least one name!")
        else:
            self.errorMsg.config(text="Please, do not insert any special characters!")




