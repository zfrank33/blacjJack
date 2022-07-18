import random

class Player(object):
    def __init__(self,name):
        self.name = name
        self.score = 0

playerIn = True
dealerIn = True

# deck of cards (7 if possible)
deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A']

dealerHand = []
player1 = []
player2 = []
player3 = []
player4 = []
player5 = []


# deal hands
players = [player1,player2,player3,player4,player5]

for player in players:
    if player.score >21:bust
def deal(turn):
    card= random.choice(deck)
    turn.append(card)
    deck.remove(card)

#  count each players hand
def total(turn):
    total=0 
    face = ['K', 'Q', 'J']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
                total+=1 
        else:
            if total > 11:
                total += 1
    return total

# figure out who one this hand
def showDealersHand():
    if len(dealerHand)==2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0], dealerHand[1]

# play it agian Sam
for _ in range(2):
    deal(dealerHand)
    deal(player1)
    deal(player2)
    deal(player3)
    deal(player4)
    deal(player5)

while playerIn or dealerIn:
    print(f"Dealer has{showDealersHand()} and X")
    print(f"You have{player1} for a total of {total(player1)}")
    if playerIn:
        hitOrStay = input("1: Stay\n 2: Hit\n")
    if total(dealerHand) > 16:
                dealerIn = False
    else:
        deal(dealerHand)
    if hitOrStay =='1':
        playerIn  = False
    else:
        deal(player1)
    else:
        deal(player2)    
    else:
        deal(player3)        
    else:
        deal(player4)    if total(player1Hand)>= 21:
    else:
        deal(player5)        break
    elif total(dealerHand) >= 21:
        break

if total(player1Hand) == 21:
    print(f"\nYou have {player1Hand} BlacJack and Dealer has {dealerHand}")
elif total(dealerHand) == 21:
    print(f"\nYou have {player1Hand} and Dealer has {dealerHand} BlacJack")
elif total(player1Hand)>21:
    print(f"\nDealer has {dealerHand} and You bust {player1Hand}! Dealer wins!") 
elif total(dealerHand)>21:
    print(f"\nYou have{player1Hand}  and Dealer {dealerHand} Busts!")
elif 21-total(dealerHand)<21-total(player1Hand):
    print(f"n\You have{player1Hand} and Dealer has{dealerHand}")
    print("Dealer wins")
elif 21 - total (dealerHand)< 21-total(player1Hand):
    print(f"\nYou have(player1Hand) and Dealer has {dealerHand}")
    print("You win!")



  # loop the game till deck dies
