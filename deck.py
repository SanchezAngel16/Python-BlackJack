from card import Card
import random

class Deck(object):
    def __init__(self):
        self.cards = []
        
 
    def get_sorted_cards(self):
        for i in range(4):
            for j in range(13):
                self.cards.append(Card(i+1,j+1))
        return self.cards

 
    def get_unsorted_cards(self):
        unsorted_cards = []
        sorted_cards_temp = self.get_sorted_cards()
        for i in range(52):
            remove_index = random.randint(0,len(sorted_cards_temp)-1)
            unsorted_cards.append(sorted_cards_temp.pop(remove_index))
        return unsorted_cards


