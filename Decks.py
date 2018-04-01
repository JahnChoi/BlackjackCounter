# Typically 1-8 decks of 52 cards in main deck

import Card

class Decks:
    def __init__(self, numOfDecks: float):
        self._staticNumOfDecks = int(numOfDecks)
        self._numOfDecks = numOfDecks   # Count to nearest half-deck
        self._percOutOfDeck = float()   # default 0.0
        self._cardDict = dict()
        self._setUp()
        
    def _setUp(self):
        '''
        Initializes Cards in Decks.
        '''
        for value in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            card = Card(value)
            self._cardDict.update(card=4*self._staticNumOfDecks)
        return
    
    def _round_to_nearest_half(self, value: float):
        '''
        Rounds and returns value to nearest 0.5.
        '''
        return round(value * 2) / 2
    
    def subtract(self, cards: list):
        '''
        Take out specific list of Cards from master deck after each round of card dealings.
        Also update self._percOutOfDeck and self._numOfDecks.
        '''
        for card in cards:
            self._cardDict[card.value] -= 1
        self._percOutOfDeck += len(cards)/self._staticNumOfDecks
        self._numOfDecks = self._round_to_nearest_half(len(self.cardList)/26)
        return
        
    def get_deck_count(self):
        '''
        Returns number of Cards in Decks as an int.
        '''
        count = 0
        for v in self._cardDict.values():
            count += v
        return count
    
    def get_remaining_count(self):
        return self._percOutOfDeck
    
    def get_remaining_cards(self, value: str):
        '''
        Returns number of remaining value cards in the master deck.
        '''
        return self._cardDict[Card(value)]
