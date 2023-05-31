class Cards(object):
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
  
  def getRank(self):
      return self.rank
  
  def getSuit(self):
    return self.suit
  
  def BJValue(self):
    if self.rank == 1:
      return 1
    elif self.rank == 11 or self.rank == 12 or self.rank == 13:
      return 10
    else:
      return self.rank
  
  def __str__(self):
    string = ""
    if self.rank == 1:
      string = "Ace of "
    elif self.rank == 11:
      string = "Jack of "
    elif self.rank == 12:
      string = "Queen of "
    elif self.rank == 13:
      string = "King of "
    else:
      string = str(self.rank) + " of " 
    
    if self.suit == "d":
      string += "Diamonds"
    elif self.suit == "c":
      string += "Clubs"
    elif self.suit == "h":
      string += "Hearts"
    else:
      string += "Spades"
    return string