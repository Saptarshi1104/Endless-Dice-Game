from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(background="yellow")

img = ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

player1_label = Label(root, text = "Player 1", bg="royal blue", fg="white")
player1_label.place(relx=0.1,rely=0.3,anchor=CENTER)

player2_label = Label(root, text = "Player 2", bg="royal blue", fg="white")
player2_label.place(relx=0.9,rely=0.3,anchor=CENTER)

player1_score_label = Label(root, bg="royal blue", fg="white")
player1_score_label.place(relx=0.1,rely=0.4,anchor=CENTER)

player2_score_label = Label(root, bg="royal blue", fg="white")
player2_score_label.place(relx=0.9,rely=0.4,anchor=CENTER)

dice_number_label = Label(root, bg="chocolate", fg="white")
dice_number_label.place(relx=0.5,rely=0.5,anchor=CENTER)

winner1 = Label(root, bg="orange", fg="black")
winner1.place(relx=0.5,rely=0.7,anchor=CENTER)

winner2 = Label(root, bg="orange", fg="black")
winner2.place(relx=0.5,rely=0.8,anchor=CENTER)

winner3 = Label(root, bg="orange", fg="black")
winner3.place(relx=0.5,rely=0.6,anchor=CENTER)

player1_score = 0
def player1():
    global player1_score
    random1 = random.randint(1,6)
    dice_number_label['text'] = "Player 1 dice random number: " + str(random1)
    player1_score = player1_score + random1
    player1_score_label['text'] = str(player1_score)
    
button1 = Button(root, image = img, command = player1)
button1.place(relx=0.1,rely=0.6,anchor=CENTER)

player2_score = 0
def player2():
    global player2_score
    random2 = random.randint(1,6)
    dice_number_label['text'] = "Player 2 dice random number: " + str(random2)
    player2_score = player2_score + random2
    player2_score_label['text'] = str(player2_score)
    
button2 = Button(root, image = img, command = player2)
button2.place(relx=0.9,rely=0.6,anchor=CENTER)   

def winner():
    if player1_score > player2_score:
        winner1['text'] = "Player 1 wins the game"
        winner2['text'] = ""
        winner3['text'] = ""
    elif player2_score > player1_score: 
        winner2['text'] = "Player 2 wins the game"
        winner1['text'] = ""
        winner3['text'] = ""
    elif player1_score == player2_score:
        winner3['text'] = "Game Drawn"
        winner1['text'] = ""
        winner2['text'] = ""

button3 = Button(root, text = "End game", command = winner, bg = "pink", fg = "black")
button3.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()