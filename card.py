from PIL import ImageTk, Image

class Card(object):
    def __init__(self, card_type, card_number):
        self.card_type = card_type
        self.card_number = card_number
        self.visible = False


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


    def get_card_graphic(self):
        imageRoute = str(self.get_card_type()) + "_" + str(self.card_number) + ".png"
        image = Image.open("BlackJack/res/cards/"+imageRoute)
        image = image.resize((80,116), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        return img

