import tkinter as tk
import json

class Leaderboard(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)

        with open('playerdata.json','r') as file:
           playerData = json.load(file)

        widthW,heightW = (800,600)

        self.title('LeaderBoard')
        self.geometry('800x600')
        self.maxsize(widthW,heightW)
        self.minsize(widthW,heightW)
        self.configure(background='#2b2b2a')
        self.resizable(0, 0)

        titleWindow = tk.Label(self,text="Leaderboard")
        titleWindow.config(font=("Helvetica",20,"bold"), bg="#2b2b2a", fg="white")
        titleWindow.place(relx=0.5,rely=0.1,anchor = tk.CENTER)

        canvas = tk.Canvas(self, bg='#2b2b2a', width=750, height=400, highlightthickness=0)
        canvas.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.place(relx=0.97, rely=0.55, anchor=tk.CENTER, height=400)

        canvas.configure(yscrollcommand=scrollbar.set)

        table_frame = tk.Frame(canvas, bg='#2b2b2a')
        canvas.create_window((0, 0), window=table_frame, anchor='nw')

        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        table_frame.bind("<Configure>", on_frame_configure)

        headers = ['Rank', 'Player Name', 'Total Score', 'Rolls', 'Average', 'Last Played']
        for col, header in enumerate(headers):
            e = tk.Entry(table_frame, width=15, fg='white', bg='black', font=('Arial', 10, 'bold'), justify='center')
            e.grid(row=0, column=col)
            e.insert(tk.END, header)

        playerData.sort(key=lambda x: x['totalscore'], reverse=True)

        rowColor = 'blue'
        for row, player in enumerate(playerData, start=1):
            values = [
                row,
                player['playername'],
                player['totalscore'],
                player['rolls'],
                round(player['totalscore'] / player['rolls'], 2) if player['rolls'] > 0 else 0,
                player['lastplayed']
            ]
            for col, value in enumerate(values):
                e = tk.Entry(table_frame, width=15, font=('Arial', 11))

                if col == 0 and value == 1:
                    rowColor = "blue"

                if col == 0 and value != 1:
                    rowColor = "black"

                e.config(fg = rowColor)
                e.grid(row=row, column=col)
                e.insert(tk.END, value)