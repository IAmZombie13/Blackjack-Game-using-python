import random as ra

#Keeps Track of Cards
cards = {
    "Ace" : {
        "Value" : 1,
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

#Used to Deal cards to player
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

#Ends the players turn
def GameSet(player):
    players[player]["GameSet"] = True
    
#If pLayer loses
def GameLost(player):
    players[player]["Lost"] = True


#GAMEPLAY STARTS HERE

#adding another player (for this code a dealer)
players.append({
        "Cards" : [],
        "Score" : 0,
        "Lost" : False,
        "GameSet" : False
    })

#dealing cards for dealer
DealCards(0)
DealCards(0)

#dealing cards for player
DealCards(1)
DealCards(1)

#game logic for getting and setting cards
while( not (players[1]["GameSet"] or players[1]["Lost"]) ):
    print("\n")
    print(f"Your Cards :{players[1]["Cards"]}")
    print("Dealers cards: ? ?")
    choice = int(input("Get Cards or Set it down(1/2):"))
    if(choice == 1):
        DealCards(1)
        if(players[1]["Score"] > 21):
            players[1]["Lost"] = True
    elif (choice == 2):
        players[1]["GameSet"] = True
    else:
        print("Ivalid choice, Choose again")


print(f"Your Cards :{players[1]["Cards"]}")
print(f"Dealers cards: {players[0]["Cards"]}")


if(players[1]["Lost"]):
    print("Dealer Won, Player went bust")
elif(players[0]["Score"] > players[1]["Score"]):
    print("Dealer Won")
elif(players[0]["Score"] < players[1]["Score"]):
    print("Player Won")
else:
    print("Its a Tie")