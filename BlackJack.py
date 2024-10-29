import random as ra

#Keeps Track of Cards
cards = {
    "Ace" : {
        "Value" : 11,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Two" : {
        "Value" : 2,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Three" : {
        "Value" : 3,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Four" : {
        "Value" : 4,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Five" : {
        "Value" : 5,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Six" : {
        "Value" : 6,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Seven" : {
        "Value" : 7,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Eight" : {
        "Value" : 8,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Nine" : {
        "Value" : 9,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Ten" : {
        "Value" : 10,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "King" : {
        "Value" : 10,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Queen" : {
        "Value" : 10,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    },
    "Jack" : {
        "Value" : 10,
        "Hearts" : True,
        "Diamonds" : True,
        "Spades" : True,
        "Clubs" : True       
    }
}
card_value = list(cards)
suite = ['Hearts', 'Diamonds', 'Spades', 'Clubs']


#initialising first player
Players = [
    {
        "Cards" : [],
        "Score" : 0,
        "Lost" : False,
        "GameSet" : False
    }
]

#Functions to use for Game

