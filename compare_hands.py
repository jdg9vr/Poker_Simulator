from one_hand import hand_detector

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
    return hand_rank.index(max(hand_rank)) # this does not handle ties
    

compare_hands([['11s', '10s'], ['14c', '13d']], ['09d', '08s', '02d', '14h', '12h'])