
import Card
import Decks

# Counting Card: Hi-Lo Algorithm:
# 1) Assign value to every card (this is done in Card.py)
# 2) "Running Count" - sum of total value based of card dealt
# 3) "True    Count" - Running count divided by the amount of decks used
#                    - Alpha Ver: ASSUME THAT THERE IS ONLY 1 DECK -> Running = True Count
# 4) Base bets on true count (Higher is better for player)

# get sum of Running Count
def get_r_count(card, r_count):
    value = card.get_count()
    r_count = r_count + value
    return r_count

# get estimated advantage percentage of player
# assume Running Count = True Count
# .5% for 6 decks blackjack game
def get_adv_percentage(r_count):
    
    if (r_count == 1):
        print("0 % Advantage: Even Game")
        
    elif (r_count > 1):
        pos_counter = r_count - 1
        percentage = pos_counter / 2
        # 1: 6 deck ratio, need to increase percentage because more variability in 1 deck
        percentage = percentage * 6
        
        if (percentage > 100):
            print("ESTIMATED 99.9% Advantage: Player's Edge")
        else:
            print("ESTIMATED", percentage, "% Advantage: Player's Edge")

    elif (r_count < 1):
        neg_counter = r_count - 1
        percentage = neg_counter / -2
        percentage = percentage * 6

        if (percentage > 100):
            print("ESTIMATED 99.9% Disadvantage: House's Edge")
        else:
            print("ESTIMATED", percentage, "% Disadvantage: House's Edge")

    else:
        print ("INVALID RUNNING COUNT")
        


    


