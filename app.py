from deck import Deck
from tkinter import *
import os

#GLOBAL VARS
w_width = 700
w_height = 500
cards_area_width = 500
cards_area_height = 500
playing_area_width = 200
playing_area_height = 500

deck = Deck()
main_deck = deck.get_unsorted_cards()
player_deck = []
house_deck = []

def on_click(event):
    print("Hola")

def set_window():
    window = Tk()
    window.title('BlackJack')
    window.maxsize(w_width, w_height)
    window.minsize(w_width, w_height)

    #Frames
    left_frame = Frame(window, width = cards_area_width, height = 500, bg='green')
    left_frame.grid(column = 0, row = 0)
    right_frame = Frame(window, width=200, height=500, bg='black')
    right_frame.grid(column = 1, row = 0)
    
    #Components for left_frame
    top_frame = Frame(left_frame, width = 500, height = 250, bg='green')
    top_frame.pack()
    ##Components for top_frame
    label = Label(top_frame, text="House", bg='green', fg='white', font=("Arial Bold", 18))
    label.place(x = 250, y = 0)

    bottom_frame = Frame(left_frame, width = 500, height = 250, bg='green')
    bottom_frame.pack()
    ##Components for bottom_frame
    label = Label(bottom_frame, text="Player", bg='green', fg='white', font=("Arial Bold", 18))
    label.place(x = 250, y = 0)
    
    n_card = get_next_card()
    image = n_card.get_card_graphic()
    panel = Label(bottom_frame, image = image)
    panel.place(x=0,y=0)
    n_card2 = get_next_card()
    image2 = n_card2.get_card_graphic()
    panel2 = Label(bottom_frame, image = image2)
    panel2.place(x=30,y=0)
    panel2.bind("<Button-1>", on_click)

    #Components for right_frame
    label = Label(right_frame, text="BlackJack", bg='black', fg='white', font=("Arial Bold", 18))
    label.place(x = 40, y = 0)

    window.mainloop()

def get_next_card():
    global main_deck
    if len(main_deck) == 0:
        main_deck = deck.get_unsorted_cards()
        return main_deck.pop()
    return main_deck.pop()


def main():
    set_window()

main()