import app
import leaderboard
import enterplayers

#def openLeaderBoard():
#    leaderboardApp = leaderboard.Leaderboard()

if __name__ == "__main__":
    enterplayersApp = enterplayers.EnterPlayers()
    enterplayersApp.mainloop()

    #diceApp = app.App()
    #diceApp.rollButton.configure(command=diceApp.rollDice)
    #diceApp.leaderBoardButton.configure(command=openLeaderBoard)
    #diceApp.mainloop()