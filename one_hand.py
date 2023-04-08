
def hand_detector(hand):
    '''
    PURPOSE: Detect the hand given the seven cards a player has
    INPUT: List - A player's 7 cards
    OUTPUT: Tuple - First element is the hand rank (i.e. 4 for Flush); second element is a list of the five cards of the hand in order given the rank
    '''
    
    # Sort hand (by number, not suit)
    sorted_hand = sorted(hand, reverse=True)
    
    # Create number and suit count dictionaries from sorted hands
    num_counts, suit_counts = create_counts(sorted_hand)
    
    # Sort these counts by their values (highest first)
    sorted_num_counts = sort_dict_by_values(num_counts)
    sorted_suit_counts = sort_dict_by_values(suit_counts)
    
    # Extract the keys and values from the counts
    nums = list(sorted_num_counts)
    counts = list(sorted_num_counts.values())
    
    suits = list(sorted_suit_counts)
    suit_count_vals = list(sorted_suit_counts.values())
    
    # Check straight to be used later
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

def create_counts(sorted_hand):
    '''
    PURPOSE: Create a count of the card numbers and suits from a given hand
    INPUT: List - Sorted 7 cards from hand_detector input
    OUTPUT: Tuple - First element is a dictionary where the keys are the number, the values are the counts; second element is a dictionary where the keys are the suit, the values are the counts
    '''
    num_counts  = {}
    suit_counts = {}
    for card in sorted_hand:
        # The number of each cards is the first two values of the string, the suit is the third value
        num = int(card[:2])
        suit = card[2]
        
        # NUMBER
        ## if the number is already in the keys of the dictionary, add one to the value
        if num in num_counts:
            num_counts[num] += 1
        else: # else create a new dictionary key and set the value to one
            num_counts[num] = 1
        
        # SUIT
        ## if the suit is already in the keys of the dictionary, add one to the value
        if suit in suit_counts:
            suit_counts[suit] += 1
        else: # else create a new dictionary key and set the value to one
            suit_counts[suit] = 1
    return num_counts, suit_counts

def sort_dict_by_values(input_dict):
    '''
    PURPOSE: Sort a dictionary by its values
    INPUT: Dictionary - Keys refer to the number/suit and the values refer to the counts of items
    OUTPUT: Dictionary - Sorted input dictionary by values
    '''
    return dict(sorted(input_dict.items(), key=lambda x:x[1], reverse=True))   
     
def check_straight(values):
    '''
    PURPOSE: Check if a hand is a straight
    INPUT: List - Unique numbers for a player's 7-card hand
    OUTPUT: Tuple - First element is a boolean, second element is either a list of the straight cards or 0 for no straight
    '''
    straight = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Sort the unique numbers (ascending)
    new = sorted(values, reverse=True)
    
    # Check if there is an Ace (14) and also all of a 5, 4, 3, and 2. If so, return True and the values
    if (14 in new) & (all(x in new for x in [5, 4, 3, 2])):
            return True, [5, 4, 3, 2, 1]
    else:
        for i in range(len(new)-4):
            for j in range(9):
                # Check each if each consecutive set of 5 in the given hand is in the straight list
                if new[i:i+5] == straight[j:j+5]:
                    return True, new[i:i+5] # If so return true and the values
        return False, 0

def output_hand(priority_values, sorted_hand, five=False):
    '''
    PURPOSE: Return cards in order of the hand (i.e. Pair of 2's with AQJ would be 22AQJ)
    INPUT: Priority_values: List - Card values/suits that have priority (card with pair, set, quads or suit with flush) in order
           Sorted_hand: List - Full original sorted hand of 5/7 cards
           Five (default=False): Boolean - Whether the priority is all 5 cards (full house or flush)
    OUTPUT: List - 5 cards as 3-character strings in order of the hand
    '''
    
    # Take each priority value and add all of those values in sorted hand to the beginning of the final output list
    final_hand = []
    for value in priority_values:
        value_cards = list(filter(lambda x: str(value) in x, sorted_hand))
        final_hand += value_cards
    
    # If 5 cards are not in the final, add the rest of the cards in order to the final list
    if ~five:
        for card in sorted_hand:
            if (card not in final_hand):
                final_hand.append(card)
    
    return final_hand[:5] # output only 5 cards each time
        