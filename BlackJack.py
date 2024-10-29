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
players = [
    {
        "Cards" : [],
        "Score" : 0,
        "Lost" : False,
        "GameSet" : False
    }
]

#FUNCTIONS TO USE FOR THE GAME

def DealCards(player):
    notDone = True
    
    #randomly selects a card value and a suite
    while notDone:  
        number = ra.randint(0,len(card_value)-1)
        type = ra.randint(0,len(suite)-1)
        #checks if that card has been taken or not
        if cards[card_value[number]][suite[type]]:
            cards[card_value[number]][suite[type]] = False
            notDone = False
    players[player]["Cards"].append(f"{card_value[number]} of {suite[type]}")
    players[player]["Score"] += cards[card_value[number]]["Value"]
