import tkinter as tk
import json

class Leaderboard(tk.Tk):
    def __init__(self):
        super().__init__()

        with open('playerdata.json','r') as file:
           playerData = json.load(file)

        widthW,heightW = (800,600)

        self.title('LeaderBoard')
        self.geometry('800x600')
        self.maxsize(widthW,heightW)
        self.minsize(widthW,heightW)
        self.configure(background='#2b2b2a')
        self.resizable(0, 0)

        headers = ['Rank', 'Player Name', 'Total Score', 'Rolls', 'Average', 'Last Played']
        for col, header in enumerate(headers):
            e = tk.Entry(self, width=15, fg='white', bg='black', font=('Arial', 14, 'bold'))
            e.grid(row=0, column=col)
            e.insert(tk.END, header)

        playerData.sort(key=lambda x: x['totalscore'], reverse=True)

        for row, player in enumerate(playerData, start=1):
            values = [
                row,
                player['playername'],
                player['totalscore'],
                player['rolls'],
                round(player['totalscore'] / player['rolls'], 2) if player['rolls'] > 0 else 0,
                "test"
            ]
            for col, value in enumerate(values):
                e = tk.Entry(self, width=15, fg='blue', font=('Arial', 12))
                e.grid(row=row, column=col)
                e.insert(tk.END, value)