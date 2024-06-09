class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"Card(rank='{self.rank}', suit='{self.suit}')"

    def __str__(self):
        return f"{self.rank} of {self.suit}"

card = Card('7', 'diamonds')

print(repr(card))  # Output: Card(rank='7', suit='diamonds')

print(str(card))   # Output: 7 of diamonds
print(card)        # Output: 7 of diamonds (print() implicitly calls str())
