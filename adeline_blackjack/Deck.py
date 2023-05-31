from Card import *
import random

class Deck(object):
  """A deck of cards"""
        
  def __init__(self):
    """Initialize the deck of cards"""
    self.cards = []
    suits = ["c","d","h","s"]

    #generate the cards
    for suit in suits:
      for rank in range(1,14):
        self.cards.append(Cards(rank,suit))
                        
  def shuffle(self):
    """Shuffle the deck"""
    random.shuffle(self.cards)
                                
  def __str__(self):
    deck_str = ""
    for card in self.cards:
      deck_str = deck_str +"\n"+ str(card)
    return deck_str
       
  def takeCard(self):
    """returns a card from the Deck and removes it from the deck
    """
    topCard = self.cards[0]
    self.cards = self.cards[1:]
    return topCard

  def reset(self):
    """ resets the deck so that the cards are grouped by suit and ordered by rank
    """
    self.__init__()