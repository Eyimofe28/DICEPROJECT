from tkinter import *
from PIL import Image, ImageTk
import random

window = Tk()
# the Tk() provides a robust and platform independent windowing toolkit(creates an instance for window).
# A window serves as a container that contains widgets(gui elements:buttons, labels and images.)
window.geometry('600x600')
window.title("DICE ROLLING GAME")
window.config(background="black")
icon = PhotoImage(file='die.png')
window.iconphoto(True, icon)


intro = Label(window, text="HELLO!",
              font=("Arial", 24, "bold"), fg="black", bg="white")
intro.place(x=250, y=50)

dice1 = ['die1.png', 'die2.png', 'die3.png', 'die4_.png', 'die5_.png', 'die6.png']
dice2 = ['die1.png', 'die2.png', 'die3.png', 'die4_.png', 'die5_.png', 'die6.png']

Die = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
Die2 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))

lab = Label(window, image=Die)
lab2 = Label(window, image=Die2)

lab.place(x=100, y=150)
lab2.place(x=350, y=150)

# player = tkvideo('rolling_dice.mp4', my_label, loop=1, size=(300, 300))
# player.play()


def roll_dice():
    ROLL = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
    ROLL2 = ImageTk.PhotoImage(Image.open(random.choice(dice2)))

    lab.configure(image=ROLL)
    lab2.configure(image=ROLL2)

    lab.image = ROLL
    lab2.image = ROLL2


roll = Button(window, text="ROLL THE DICE!",
              font=("Bell MT", 20, "bold"),
              fg="dark blue", activeforeground="dark blue",
              bg="white", activebackground="white",
              command=roll_dice)
roll.place(x=200, y=400)

end = Button(window, text="EXIT", font=("Arial", 20, "bold"),
             background="dark red", activebackground="dark red",
             foreground="white", activeforeground="white",
             command=exit)
end.place(x=270, y=500)

window.mainloop()
