import collections
from random import choice

Cards = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Cards(rank, suit) for suit in self.suit for rank in self.rank] # list of Cards
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position): # The __getitem__ delegate to the [] operator of self._cards, our deck is iterable
        return self._cards[position]

deck = FrenchDeck()

## example of using named tuple
wine_card = Cards('7', 'diamonds')
print(wine_card)

print(deck[0]) # thanks to __getitem__ method

# Slicing
print("Slicing: ", deck[:3])

# Iterating
#for card in deck:
    #print(card)

# random choice
print("Supports randon choice", choice(deck))

