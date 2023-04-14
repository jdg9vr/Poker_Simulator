from one_hand import hand_detector
from itertools import compress
import numpy as np

def compare_hands(list_of_hands, community_cards):
    '''
    PURPOSE: Give the winner of a group of hands (no limit on number of players)
    INPUT: List_of_hands: List - Lists of pocket cards of all players
           Community_cards: List - The five community cards
    OUTPUT: List - Index of the winning hand(s) from the list_of_hands (usually only 1)
    '''
    # Create a list of 7 cards for each player from the inputted pockets and community cards
    full_hands = []
    for hand in list_of_hands:
        full_hands.append(hand+community_cards)
        
    # Find the value of the hand with hand_detector and create a list of the rank and a list for the cards in order
    hand_rank = []
    cards_in_order = []
    for hand in full_hands:
        hand_outcome = hand_detector(hand)
        hand_rank.append(hand_outcome[0])
        cards_in_order.append(hand_outcome[1])
    
    # Find the best rank and the boolean of the best rank
    best_hand = max(hand_rank)
    which_best = [i == best_hand for i in hand_rank]
    
    if sum(which_best) == 1: # if the amount of hands with the max best rank is one (only one winner no ties)
        print(f"Hand {hand_rank.index(best_hand)} wins!")
        return hand_rank.index(best_hand) # return the index of that best hand
    else: # tie
        # Create a tie hands list
        tie_hands = list(compress(cards_in_order, which_best))
        print(tie_hands)
        handle_tie(best_hand, tie_hands, which_best) # send to handle tie function
    
def handle_tie(rank, hands, tie_index_bools):
    '''
    PURPOSE: Return the best hand(s) from all the tied hands
    INPUT: Rank: Int - The rank of the tied hands (integer represented a specific hand i.e. 4 = Flush)
           Hands: List - Tied hands in order where each element is a hand (string form or int form for straights)
           Tie_index_bools: List - Booleans representing which of the original hands are tied
    OUTPUT: List - Index of the winning hand(s) from the list_of_hands (1 unless tie)
    '''
    # Get indexes from the original list of the ties
    tie_index = list(np.where(tie_index_bools)[0])
    
    # If the hands are strings, extract the actual numbers (want this even for flushes)
    if type(hands[0]) == str:
        real_hands = []
        for hand in hands:
            real_hand = []
            for card in hand:
                real_hand.append(int(card[:2])) # append the first two characters as an int to get the number
            real_hands.append(real_hand)
    else:
        real_hands = hands
        
    # STRAIGHT FLUSH
    if rank == 1:
        first_cards = list(list(zip(*real_hands))[0])
        max_straight_card = max(first_cards)
        which_high_straight = [i == max_straight_card for i in first_cards]
        
        if sum(which_high_straight) == len(first_cards):
            print(f"Tie between {list(compress(tie_index, which_high_straight))}!")
            return list(compress(tie_index, which_high_straight))
    return 

# 1: straight, 2: pair
compare_hands([['11s', '10s'], ['14c', '13d']], ['09d', '08s', '02d', '14h', '12h'])

# 1: pair of 9's, 2: pair of Aces
compare_hands([['11s', '09s'], ['14c', '13d']], ['09d', '08s', '02d', '14h', '12h'])