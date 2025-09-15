import app
import leaderboard
import enterplayers

def openLeaderBoard():
    leaderboardApp = leaderboard.Leaderboard()
    leaderboardApp.grab_set()

def startGame():
    if not enterplayersApp.combobox['values']:
        enterplayersApp.errorMsg.config(text="Please, insert at least one name!")
    else:
        enterplayersApp.destroy()
        diceApp = app.App()
        diceApp.rollButton.configure(command=diceApp.rollDice)
        diceApp.leaderBoardButton.configure(command=openLeaderBoard)
        diceApp.countdown()
        diceApp.mainloop()

if __name__ == "__main__":
    enterplayersApp = enterplayers.EnterPlayers()
    enterplayersApp.addUserButton.configure(command=enterplayersApp.enterPlayers)
    enterplayersApp.startButton.configure(command=startGame)
    enterplayersApp.mainloop()

