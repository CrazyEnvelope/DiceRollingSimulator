import tkinter as tk
from multiprocessing.connection import answer_challenge
from tkinter import PhotoImage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #window setup
        self.title('Dice Rolling Simulator')
        self.geometry('800x600')
        self.maxsize(800,600)
        self.minsize(800,600)
        self.configure(background='#2b2b2a')
        self.resizable(0,0)

        #content setup
        self.diceNumber = tk.Label(self,text = 0)
        self.diceNumber.config(font=("Arial",25), fg = "white", bg="#2b2b2a")
        self.diceNumber.place(relx = 0.5, rely=0.1, anchor=tk.CENTER)

        self.faceImage = PhotoImage(file = r"E:\Projects\DiceRollingSimulator\img\dice_faces\Side_1_Pips.png")
        self.faceImageDice = self.faceImage.subsample(3,3)
        tk.Label(self , image = self.faceImageDice).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.rollButton = tk.Button(self,text='Roll')
        self.rollButton.place(relx = 0.5, rely = 0.88, anchor=tk.CENTER)




