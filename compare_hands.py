from one_hand import hand_detector
from itertools import compress
import numpy as np

def compare_hands(list_of_hands, community_cards):
    full_hands = []
    for hand in list_of_hands:
        full_hands.append(hand+community_cards)
    hand_rank = []
    cards_in_order = []
    for hand in full_hands:
        hand_outcome = hand_detector(hand)
        hand_rank.append(hand_outcome[0])
        cards_in_order.append(hand_outcome[1])
    
    best_hand = max(hand_rank)
    which_best = [i == best_hand for i in hand_rank]
    if len(np.where(which_best)[0]) == 1:
        print(f"Hand {hand_rank.index(best_hand)} wins!")
        return hand_rank.index(best_hand)
    else:
        tie_hands = list(compress(cards_in_order, which_best))
        print(tie_hands)
        handle_tie(best_hand, tie_hands, which_best)
    
def handle_tie(rank, hands, tie_index_bools):
    tie_index = list(np.where(tie_index_bools)[0])
    
    if type(hands[0]) == str:
        real_hands = []
        for hand in hands:
            real_hand = []
            for card in hand:
                real_hand.append(int(card[:2]))
            real_hands.append(real_hand)
    else:
        real_hands = hands
        
    
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