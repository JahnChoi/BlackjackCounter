
import Card
import Algorithm

# Algorithms' Functions:
# r_count = Algorithm.get_r_count(card, r_count)
# Algorithm.get_adv_percentage(r_count)

#TESTING
r_count = 0
loop = 1
while (loop == 1):
    
    card_input = input("Enter card drawn: ")
    card = Card.Card(card_input)

    r_count = Algorithm.get_r_count(card, r_count)
    print(r_count)

    Algorithm.get_adv_percentage(r_count)

    exit_input = input("Exit? (y/n): ")
    if (exit_input == 'y'):
        loop = 0
    elif (exit_input == 'n'):
        loop = 1
    else:
        print("Invalid input, continuing...")
        loop = 1
        
    
    
    



