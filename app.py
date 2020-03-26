from deck import Deck
import pygame
import os
from gui_components import custom_button

#GLOBAL VARS

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)

s_width = 700
s_height = 500

deck = Deck()
main_deck = deck.get_unsorted_cards()
player_deck = []
dealer_deck = []

win = pygame.display.set_mode((s_width, s_height))
pygame.font.init()
hit_button = custom_button(white, 10, 450, 100, 20, "Hit")
stand_button = custom_button(white, 150, 450, 100, 20, "Stand")

def get_next_card():
    global main_deck
    if len(main_deck) == 0:
        main_deck = deck.get_unsorted_cards()
        return main_deck.pop()
    return main_deck.pop()

def redraw_window(win, player_deck, dealer_deck):
    win.fill((0,200,0))
    player_score = 0
    dealer_score = 0 
    #Draw card decks
    x_pos = 10
    ##Draw dealer cards
    for card in dealer_deck:
        win.blit(card.get_graphic_card(), (x_pos,90))
        x_pos += 80 + 5
        dealer_score += card.card_value

    ##Draw player cards
    x_pos = 10
    for card in player_deck:
        win.blit(card.get_graphic_card(), (x_pos,260))
        x_pos += 80 + 5

    #Draw texts
    font = pygame.font.SysFont('comicsans', 30)
    blackjack_text = font.render("BlackJack", 1, (0,0,0))
    win.blit(blackjack_text, (10,10))
    dealer_text = font.render("Dealer: " + str(dealer_score), 1, (0,0,0))
    win.blit(dealer_text, (10,60))
    player_text = font.render("Player: " + str(player_score), 1, (0,0,0))
    win.blit(player_text, (10,230))

    #Draw hit and stand buttons
    hit_button.draw(win, (0,0,0))
    stand_button.draw(win, (0,0,0))


def main():
    run = True
    card = get_next_card()
    card.visible = True
    dealer_deck.append(card)
    card = get_next_card()
    card.visible = True
    dealer_deck.append(card)
    while run:
        redraw_window(win, player_deck, dealer_deck)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hit_button.isOver(pos):
                    print("hit was clicked")
                if stand_button.isOver(pos):
                    print("stand was clicked")
            if event.type == pygame.MOUSEMOTION:
                if hit_button.isOver(pos):
                    hit_button.color = red
                else:
                    hit_button.color = white
                if stand_button.isOver(pos):
                    stand_button.color = red
                else:
                    stand_button.color = white      
    pygame.display.quit()

main()