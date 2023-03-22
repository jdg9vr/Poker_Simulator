
def create_counts(sorted_hand):
    num_counts  = {}
    suit_counts = {}
    for card in sorted_hand:
        num = int(card[:2])
        suit = card[2]
        
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
            
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    return num_counts, suit_counts

        
def check_straight(sorted_values):
    new = sorted(sorted_values, reverse=True)
    straight = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    if (14 in new) & (all(x in new for x in [5, 4, 3, 2])):
            return True, [5, 4, 3, 2, 1]
    else:
        for i in range(len(new)-4):
            for j in range(9):
                if new[i:i+5] == straight[j:j+5]:
                    return True, new[i:i+5]
        return False, 0

def sort_dict_by_values(input_dict):
    return dict(sorted(input_dict.items(), key=lambda x:x[1], reverse=True))

def output_hand(priority_values, sorted_hand, five=False):
    final_hand = []
    for value in priority_values:
        value_cards = list(filter(lambda x: str(value) in x, sorted_hand))
        final_hand += value_cards
    
    if ~five:
        for card in sorted_hand:
            if (card not in final_hand):
                final_hand.append(card)
                
    return final_hand[:5]
        
        
def hand_detector(hand):
    # Sort hand (by number, not suit)
    sorted_hand = sorted(hand, reverse=True)
    
    # Create number and suit counts from sorted hands
    num_counts, suit_counts = create_counts(sorted_hand)
    
    # Sort these counts by their values (highest first)
    sorted_num_counts = sort_dict_by_values(num_counts)
    sorted_suit_counts = sort_dict_by_values(suit_counts)
    
    # Extract the keys and values from the counts
    nums = list(sorted_num_counts)
    counts = list(sorted_num_counts.values())
    
    suits = list(sorted_suit_counts)
    suit_count_vals = list(sorted_suit_counts.values())
    
    straight_tf, straight_vals = check_straight(nums)
    
    # FOUR OF A KIND
    if 4 == counts[0]:
        print("Four of a Kind!")
        final_hand = output_hand([nums[0]], sorted_hand)
        return 2, final_hand
    
    # FULL HOUSE
    elif (3 == counts[0]) & ((3 == counts[1]) | (2 == counts[1])):
        print("Full House!")
        final_hand = output_hand([nums[0], nums[1]], sorted_hand, five=True)
        return 3, final_hand
    
    # STRAIGHT FLUSH AND FLUSH
    elif suit_count_vals[0] > 4: # check if largest suit counts is 5 or more
        flush_suit = suits[0] # get the largest suit
        flush_cards = [card for card in sorted_hand if flush_suit in card] # get the cards with these suits
        straight_flush_tf, straight_flush_vals = check_straight([int(x[:2]) for x in flush_cards])
        
        if straight_flush_tf: # check straights for these cards
            print("Straight Flush!") # if these cards have a straight, it is a straight flush
            return 1, straight_flush_vals
        else:
            print("Flush!") # if not it is a normal flush
            final_hand = output_hand([suits[0]], sorted_hand, five=True)
            return 4, final_hand
    
    # STRAIGHT
    elif straight_tf: #Straight
        print("Straight!")
        return 5, straight_vals
    
    # THREE OF A KIND
    elif 3 == counts[0]:
        print("Three of a Kind!")
        final_hand = output_hand([nums[0]], sorted_hand)
        return 6, final_hand
    
    # TWO PAIR AND PAIR
    elif 2 == counts[0]:
        if 2 == counts[1]:
            print("Two Pair!")
            final_hand = output_hand([nums[0], nums[1]], sorted_hand)
            return 7, final_hand
        else:
            print("Pair!")
            final_hand = output_hand([nums[0]], sorted_hand)
            return 8, final_hand
    else:
        print("High Card!")
        final_hand = output_hand([], sorted_hand)
        return 9, final_hand