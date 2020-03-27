from deck import Deck
import pygame
import os
from gui_components import custom_button
from player import Player

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

player = Player([], 0)
dealer = Player([], 0)

win = pygame.display.set_mode((s_width, s_height))
pygame.font.init()
clock = pygame.time.Clock()
hit_button = custom_button(white, 10, 450, 100, 20, "Hit")
stand_button = custom_button(white, 150, 450, 100, 20, "Stand")


def get_next_card():
    global main_deck
    if len(main_deck) == 0:
        main_deck = deck.get_unsorted_cards()
        return main_deck.pop()
    return main_deck.pop()


def redraw_window(win):
    win.fill((0,200,0))
    player.score = 0
    dealer.score = 0
    extra_dealer_score = 0
    #Draw card decks
    x_pos = 10
    ##Draw dealer cards
    for card in dealer.deck:
        win.blit(card.get_graphic_card(), (x_pos,90))
        x_pos += 80 + 5
        dealer.score += card.card_value
        if not card.visible:
            extra_dealer_score = card.card_value

    ##Draw player cards
    x_pos = 10
    for card in player.deck:
        win.blit(card.get_graphic_card(), (x_pos,260))
        x_pos += 80 + 5
        player.score += card.card_value

    #Draw texts
    font = pygame.font.SysFont('comicsans', 30)
    blackjack_text = font.render("BlackJack", 1, (0,0,0))
    win.blit(blackjack_text, (10,10))
    dealer_text = font.render("Dealer: " + str((dealer.score - extra_dealer_score)), 1, (0,0,0))
    win.blit(dealer_text, (10,60))
    player_text = font.render("Player: " + str(player.score), 1, (0,0,0))
    win.blit(player_text, (10,230))

    #Draw hit and stand buttons
    hit_button.draw(win, (0,0,0))
    stand_button.draw(win, (0,0,0))


def set_initial_cards():
    card = get_next_card()
    card.visible = False
    dealer.deck.append(card)
    card = get_next_card()
    card.visible = True
    player.deck.append(card)
    card = get_next_card()
    card.visible = True
    dealer.deck.append(card)
    card = get_next_card()
    card.visible = True
    player.deck.append(card)


def stand_action():
    player.stand = True
    dealer.deck[0].visible = True
    while dealer.score <= 16:
        card = get_next_card()
        card.visible = True
        dealer.score += card.card_value
        dealer.deck.append(card)
    if player.score > dealer.score and player.score <= 21:
        print("Player won")
    else:
        print("Dealer won")
    

def hit_action():
    if player.score >= 21 or player.stand:
        return
    card = get_next_card()
    card.visible = True
    player.deck.append(card)


def main():
    run = True
    set_initial_cards()
    while run:
        redraw_window(win)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hit_button.isOver(pos):
                    hit_action()
                if stand_button.isOver(pos):
                    stand_action()
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