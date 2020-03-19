class Card(object):
    def __init__(self, card_type, card_number):
        self.card_type = card_type
        self.card_number = card_number
        self.visible = False
    def get_card_info_str(self):
        return f"{get_card_type(self.card_type)} {self.card_number} {self.visible}"
    def get_card_info(self):
        return (get_card_type(self.card_type), self.card_number, self.visible)

def get_card_type(card_type):
    switcher = {
        1: 'Hearts',
        2: 'Diamonds',
        3: 'Spades',
        4: 'Clubs'
    }
    return switcher.get(card_type, 'Invalid card type')