from Card import *

class Player(object):
  '''
  represents a player object
  '''
  nameStr = ''

  def __init__(self, nameStr):
    self.hand=[]  #a collection of cards
    self.score = 0  #the initial score
    self.nameStr = nameStr
    '''
    nameStr - the name of the player, i.e 'Player 1' or 'Dealer'
    '''
  
    
        
  def addToHand(self, newCard):
    '''
    appends a card object to the players hand and updates the score
        
    newCard - a card object to add to the hand
    return None
    '''
    self.hand.append(newCard)
    self.getBJScore()
    
  def getBJScore(self):
    '''
    returns the score of the players hand
        
    return int
    '''
    self.score=0
    for card in self.hand:
      self.score+=card.BJValue()
    return self.score
  
  
  def getName(self):
    '''
    returns the name of the player
    return - str
    '''
    return self.nameStr
  
        
  def __str__(self):
    '''
    returns the string representation of the object, that includes the 
    name, score, and cards in the hand
        
    return - str
    '''
    string1 = ""
    for item in self.hand:
      string1 = string1 + item.__str__() + "\n"
   
    return "Name: {0:1}\nScore: {1:1}\nCards in Hand:\n{2:1}".format(self.nameStr, str(self.getBJScore()), string1)


