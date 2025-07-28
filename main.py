import app
import functions

if __name__ == "__main__":
    app = app.App()
    app.rollButton.configure(command=app.rollDice)
    app.mainloop()