# What is a class?
# What is an instance?
# What is encapsulation?
# What is abstraction?
# What is inheritance?
# What is multiple inheritance?
# What is polymorphism?
# What is method resolution order or MRO?


import random
class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
                self.cards.append((suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            print("The deck is empty. Cannot deal any more cards.")
            return None
        else:
            return self.cards.pop()

# Test the Deck class
deck = Deck()
print("Initial deck:", deck.cards)
deck.shuffle()
print("Shuffled deck:", deck.cards)
print("Dealing a card:", deck.deal())
print("Remaining cards in the deck:", deck.cards)
