from Deck import *
from Player import *
from Card import *


class BlackJack(object):
  '''
  classdocs
  '''
  gamedeck = Deck()

  def __init__(self, playerName):
    '''
    Initializes the game by 
    - shuffling the deck
    - initializing a player1 (with given playerName) and dealer object (both are Player objects)
    '''
    self.gamedeck.shuffle()
    self.playerName = playerName
    self.player1 = Player(self.playerName)
    self.dealer = Player("Dealer")
  
  def getWinner(self):
    '''
    returns the player object (either the class's player1 or dealer object) that is the winner
    based on their hands (closest to 21 without going over)
        
    return - Player object
    ''' 
    if self.dealer.getBJScore() and self.player1.getBJScore() < 21:
      if (21 - self.dealer.getBJScore()) < (21-self.player1.getBJScore()):
        print ("The winner is: "+self.dealer.getName()+"\n")
        print (self.player1)
        print (self.dealer)
      elif self.dealer.getBJScore() == self.player1.getBJScore():
        print ("Tie!\n")
        print (self.player1)
        print (self.dealer)
      else:
        print ("The winner is: "+self.player1.getName()+"\n")
        print (self.player1)
        print (self.dealer)
    
    elif self.dealer.getBJScore() and self.player1.getBJScore() > 21:
      if (self.dealer.getBJScore() - 21) < (self.player1.getBJScore() - 21):
        print ("The winner is: "+self.dealer.getName()+"\n")
        print (self.player1)
        print (self.dealer)
      elif self.dealer.getBJScore() == self.player1.getBJScore():
        print ("Tie!\n")
        print (self.player1)
        print (self.dealer)
      else:
        print ("The winner is: "+self.player1.getName()+"\n")
        print (self.player1)
        print (self.dealer)
    
    elif self.dealer.getBJScore() or self.player1.getBJScore() > 21:
      if self.dealer.getBJScore() < 21 and self.player1.getBJScore() > 21:
        print ("The winner is: "+self.dealer.getName()+"\n")
        print (self.player1)
        print (self.dealer)
      elif self.dealer.getBJScore() == self.player1.getBJScore():
        print ("Tie!\n")
        print (self.player1)
        print (self.dealer)
      else:
        print ("The winner is: "+self.player1.getName()+"\n")
        print (self.player1)
        print (self.dealer)
    
    elif self.dealer.getBJScore() or self.player1.getBJScore() == 21:
      if self.dealer.getBJScore() == 21 and self.player1.getBJScore() != 21:
        print ("The winner is: "+self.dealer.getBJScore()+"\n")
        print (self.player1)
        print (self.dealer)
      elif self.dealer.getBJScore() == self.player1.getBJScore():
        print ("Tie!\n") 
        print (self.player1)
        print (self.dealer)
      else:
        print("The winner is: "+self.player1.getBJValue()+"\n")
        print (self.player1)
        print (self.dealer)
    
    play_Again = input("\nWould you like to play again?: ").lower()
    if play_Again == "yes":
      self.gamedeck.reset()
      game = BlackJack(self.playerName)
      game.play()
    else:
      print ("\nGoodbye! Thanks for playing!!")
  
  def showWelcome(self):
      print ("Welcome to Blackjack " + self.playerName + "!")

  def play(self):
    '''
    play the game using the class's deck, player1, and dealer objects
    '''
        
    '''
    initialize player1 and dealer hands (2 cards each)
    show player 1 hand
    player1 decision (hit or stand)
    dealer complete hand
    present game outcome - player1 win or lose
    '''
    self.showWelcome()
    for i in range(2):
      self.player1.addToHand(self.gamedeck.takeCard())
      self.dealer.addToHand(self.gamedeck.takeCard())
    
    if self.dealer.getBJScore() < 17:
      self.dealer.addToHand(self.gamedeck.takeCard())

    print (self.player1)
    

    hitOrStand = input("\nWould you like to hit or stand?: ").lower()
    while hitOrStand == "hit":
      self.player1.addToHand(self.gamedeck.takeCard())
      print (self.player1)
      
      hitOrStand = input("\nWould you like to hit or stand?: ").lower()
    self.getWinner()
