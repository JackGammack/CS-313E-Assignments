#  File: Poker.py

#  Description: Simulates a game of poker

#  Student's Name: Jack Gammack

#  Student's UT EID: jg64475

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 2/7/2018

#  Date Last Modified: 2/10/2018

import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12
    
    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    print()
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + ": " + hand)
    print()
    # determine the type of each hand and print
    points_hand = []  # create list to store points for each hand
    for i in range( len(self.players) ):
        if ( self.is_royal( self.players[i] ) ):
            points_hand.append( 10 )
            print( 'Player ' + str(i+1) + ': Royal Flush' )
        elif ( self.is_straight_flush( self.players[i] ) ):
            points_hand.append( 9 )
            print( 'Player ' + str(i+1) + ': Straight Flush' )
        elif ( self.is_four_kind( self.players[i] ) ):
            points_hand.append( 8 )
            print( 'Player ' + str(i+1) + ': Four of a Kind' )
        elif ( self.is_full_house( self.players[i] ) ):
            points_hand.append( 7 )
            print( 'Player ' + str(i+1) + ': Full House' )
        elif ( self.is_flush( self.players[i] ) ):
            points_hand.append( 6 )
            print( 'Player ' + str(i+1) + ': Flush' )
        elif ( self.is_straight( self.players[i] ) ):
            points_hand.append( 5 )
            print( 'Player ' + str(i+1) + ': Straight' )
        elif ( self.is_three_kind( self.players[i] ) ):
            points_hand.append( 4 )
            print( 'Player ' + str(i+1) + ': Three of a Kind' )
        elif ( self.is_two_pair( self.players[i] ) ):
            points_hand.append( 3 )
            print( 'Player ' + str(i+1) + ': Two Pair' )
        elif ( self.is_one_pair( self.players[i] ) ):
            points_hand.append( 2 )
            print( 'Player ' + str(i+1) + ': One Pair' )
        elif ( self.is_high_card( self.players[i] ) ):
            points_hand.append( 1 )
            print( 'Player ' + str(i+1) + ': High Card' )
    print()
    # determine winner and print
    winners = []
    winners_points = []
    for i in range( len(points_hand) ):
        if ( points_hand[i] == max(points_hand) ):
            winners.append( i )
            winners_points.append( points_hand[i] )
    if ( len(winners) == 1 ):
        print ( 'Player ' + str(winners[0]+1) + ' wins.' )
    else:
        for i in range( len(winners_points) ):
            c1 = self.players[winners[i]][0].rank
            c2 = self.players[winners[i]][1].rank
            c3 = self.players[winners[i]][2].rank
            c4 = self.players[winners[i]][3].rank
            c5 = self.players[winners[i]][4].rank
            winners_points[i] = winners_points[i] * 13**5 + c1 * 13**4 + c2 * 13**3 + c3 * 13**2 + c4 * 13 + c5 
        for j in range( len(winners) ):
                print( 'Player ' + str( winners[ winners_points.index(max(winners_points)) ] + 1) + ' ties.' )
                del winners[ winners_points.index(max(winners_points)) ]
                del winners_points[ winners_points.index(max(winners_points)) ]
                   
            

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14-i)

    if (not rank_order):
      return False

    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    
    return (same_suit and rank_order)

  def is_straight_flush (self, hand):
    rank_order = True
    for i in range (1,len(hand)):
      rank_order = rank_order and (hand[i-1].rank == hand[i].rank+1)

    if (not rank_order):
      return False

    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    
    return (same_suit and rank_order)


  def is_four_kind (self, hand):
    for i in range( len(hand) - 3 ):
        if ( hand[i] == hand[i+1] == hand[i+2] == hand[i+3] ):
            return True
    return False

  def is_full_house (self, hand):
    return ( (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]) or (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]) )

  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    return same_suit

  def is_straight (self, hand):
    rank_order = True
    for i in range (1,len(hand)):
      rank_order = rank_order and (hand[i-1].rank == hand[i].rank+1)    
    return rank_order

  def is_three_kind (self, hand):
    for i in range ( len(hand)-2 ):
        if ( hand[i] == hand[i+1] == hand[i+2] ):
            return True
    return False

  def is_two_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i] == hand[i + 1]):
        handminus = []
        for j in range( len(hand) ):
            handminus.append(hand[j])
        del handminus[i+1]
        del handminus[i]
        return self.is_one_pair(handminus)
    return False

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for k in range (len(hand) - 1):
      if (hand[k] == hand[k + 1]):
        return True
    return False

  
  def is_high_card (self, hand):
    return True

def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()

main()
