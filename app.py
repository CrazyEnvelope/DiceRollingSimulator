import tkinter as tk
from tkinter import PhotoImage
import customtkinter
import random
import json
import datetime

playerData = []

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.imgDiceLoc = {
            1: "./img/dice_faces/Side_1_Pips.png",
            2: "./img/dice_faces/Side_2_Pips.png",
            3: "./img/dice_faces/Side_3_Pips.png",
            4: "./img/dice_faces/Side_4_Pips.png",
            5: "./img/dice_faces/Side_5_Pips.png",
            6: "./img/dice_faces/Side_6_Pips.png"
        }

        widthW,heightW = (800,600)
        widthC,heightC = (340,340)

        global playerData
        with open('playerdata.json','r') as file:
           playerData = json.load(file)

        numberOfPlayers = len(playerData)
        #window setup
        self.title('Dice Rolling Simulator')
        self.geometry('800x600')
        self.maxsize(widthW,heightW)
        self.minsize(widthW,heightW)
        self.configure(background='#2b2b2a')
        self.resizable(0,0)

        #content setup
        self.diceNumber = tk.Label(self,text = 0)
        self.diceNumber.config(font=("Arial",25), fg = "white", bg="#2b2b2a")
        self.diceNumber.place(relx = 0.5, rely=0.1, anchor=tk.CENTER)

        self.faceImage = PhotoImage(file = r"./img/dice_faces/Side_1_Pips.png")
        self.faceImageDice = self.faceImage.subsample(3,3)
        self.canvas = tk.Canvas(self,bg="#2b2b2a",width=widthC,height=heightC, highlightthickness=0)
        self.canvas_image_id = self.canvas.create_image(widthC/2,heightC/2,image = self.faceImageDice)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.rollButton = customtkinter.CTkButton(
            self,
            text='Roll!',
            border_color='white',
            border_width=3,
            border_spacing=10,
            corner_radius=50,
            font=("Arial",24),
            height = 50,
            width = 150
        )
        self.rollButton.place(relx = 0.5, rely = 0.88,anchor=tk.CENTER)

        self.leaderBoardButton = customtkinter.CTkButton(
            self,
            text='Leaderboard',
            border_color='white',
            border_width=3,
            border_spacing=10,
            corner_radius=50,
            font=("Arial", 24),
            height=50,
            width=150
        )
        self.leaderBoardButton.place(relx=0.2, rely=0.88, anchor=tk.CENTER)

        self.changeBackgroundButton = customtkinter.CTkButton(
            self,
            text='Change Theme!',
            border_color='white',
            border_width=3,
            border_spacing=10,
            corner_radius=50,
            font=("Arial", 24),
            height=50,
            width=150
        )

        self.changeBackgroundButton.place(relx = 0.8, rely = 0.88,anchor=tk.CENTER)

        self.nextPlayer = tk.Label(self, text=f"Next Player:")
        self.nextPlayer.config(font=("Arial", 18), fg="white", bg="#2b2b2a")
        self.nextPlayer.place(relx=0.85, rely=0.5, anchor=tk.CENTER)

        self.currentPlayer = tk.Label(self, text=f"Current Player:")
        self.currentPlayer.config(font=("Arial", 18), fg="white", bg="#2b2b2a")
        self.currentPlayer.place(relx=0.15, rely=0.5, anchor=tk.CENTER)

        if numberOfPlayers == 1:
            self.firstPlayer = playerData[0]
            self.currentPlayer.config(text=f"Current Player:\n {self.firstPlayer['playername']}")
            self.nextPlayer.config(text=f"Next Player:\n {self.firstPlayer['playername']}")
        else:
            self.firstPlayer = playerData[0]
            self.secondPlayer = playerData[1]
            self.currentPlayer.config(text=f"Current Player:\n {self.firstPlayer['playername']}")
            self.nextPlayer.config(text=f"Next Player:\n {self.secondPlayer['playername']}")



    def rollDice(self):
        self.rollButton.configure(state = "disabled")

        numbers = [1,2,3,4,5,6]
        random.shuffle(numbers)

        self.diceNumber.config(text="Waiting...")

        for i, number in enumerate(numbers):
            self.after(i * 150, lambda num=number:self.rollAnimation(num))

        final = numbers[len(numbers)-1]
        self.after(len(numbers) * 150, lambda: self.finishRoll(final))
        self.updatePlayerData(final)

    def updatePlayerData(self,number):
        global playerData
        with open('playerdata.json', 'r') as file:
            playerData = json.load(file)

        current_name = self.currentPlayer.cget("text").replace("Current Player:\n ", "")
        tempPlayerData = {}
        for i,player in enumerate(playerData):
            if player['playername'] == current_name:
                current_time = datetime.datetime.now()
                tempPlayerData = {
                    'rank' : 0,
                    'playername' : current_name,
                    'totalscore' : player['totalscore'] + number,
                    'rolls' : player['rolls'] + 1,
                    'lastplayer' : f"{current_time.year}-{current_time.month}-{current_time.day} {current_time.hour}:{current_time.minute}"
                }
                del playerData[i]
                break
        playerData.append(tempPlayerData)
        with open('playerdata.json', 'w') as file:
            json.dump(playerData, file, indent=4)




    def rollAnimation(self,number):
        self.newfaceImageDice = PhotoImage(file=self.imgDiceLoc[number]).subsample(3, 3)
        self.canvas.itemconfig(self.canvas_image_id, image=self.newfaceImageDice)
        self.faceImageDice = self.newfaceImageDice

    def finishRoll(self,final):
        self.diceNumber.config(text=str(final))
        self.rollButton.configure(state="normal")



