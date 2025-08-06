import app
import leaderboard
import enterplayers

def openLeaderBoard():
    leaderboardApp = leaderboard.Leaderboard()

def startGame():
    diceApp = app.App()
    diceApp.rollButton.configure(command=diceApp.rollDice)
    diceApp.leaderBoardButton.configure(command=openLeaderBoard)
    diceApp.mainloop()

if __name__ == "__main__":
    enterplayersApp = enterplayers.EnterPlayers()
    enterplayersApp.addUserButton.configure(command=enterplayersApp.enterPlayers)
    enterplayersApp.startButton.configure(command=startGame)
    enterplayersApp.mainloop()

