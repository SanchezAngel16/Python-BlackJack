import pygame

class Card(object):
    def __init__(self, card_type, card_number, card_value):
        self.card_type = card_type
        self.card_number = card_number
        self.visible = False
        self.card_value = card_value


    def get_card_info_str(self):
        return f"{self.get_card_type()} {self.card_number} {self.visible}"


    def get_card_info(self):
        return (self.get_card_type(), self.card_number, self.visible)


    def get_card_type(self):
        switcher = {
            1: 'Hearts',
            2: 'Diamonds',
            3: 'Spades',
            4: 'Clubs'
        }
        return switcher.get(self.card_type, 'Invalid card type')


    def get_graphic_card(self):
        if self.visible:
            imageRoute = str(self.get_card_type()) + "_" + str(self.card_number) + ".png"
            #image = Image.open("BlackJack/res/cards/"+imageRoute)
            image = pygame.image.load("BlackJack/res/cards/"+imageRoute) 
        else:
            image = pygame.image.load("BlackJack/res/cards/reverse_card.png")
        image = pygame.transform.scale(image, (80, 116))
        return image

