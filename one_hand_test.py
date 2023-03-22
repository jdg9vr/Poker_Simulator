from one_hand import hand_detector

# Four of a kind of 3's
hand_detector(['03d', '11d', '03c', '02d', '03s', '09h', '03h'])

# High card (Ace)
hand_detector(['03d', '11d', '05c', '14d', '02s', '09h', '06h'])

# Pair of 5's
hand_detector(['03d', '05d', '05c', '14d', '02s', '09h', '06h'])

# Two pair - 5's and 2's
hand_detector(['03d', '05d', '05c', '02d', '02s', '09h', '06h'])

# Two pair - 6's and 5's (also irrelevant 2's)
hand_detector(['03d', '05d', '05c', '02d', '02s', '06h', '06h'])

# Three of a Kind of 5's
hand_detector(['03d', '05d', '05c', '05h', '02s', '09h', '06h'])

# Straight (with an irrelevant pair of 6's)
hand_detector(['03d', '05d', '04c', '07d', '06s', '09h', '06h'])

# Different Straight
hand_detector(['03d', '05d', '04c', '14d', '02s', '14h', '06h'])

# Flush
hand_detector(['03d', '05d', '04d', '14d', '02c', '13d', '06h'])

# Straight Flush with irrelevant pair
hand_detector(['03d', '05d', '04d', '14d', '02d', '14c', '06d'])

# Straight Flush with irrelevant three of a kind
hand_detector(['03d', '05d', '04d', '06d', '02d', '06c', '06h'])

# Full House (set of 6's and pair of 5's)
hand_detector(['03c', '05c', '05s', '06c', '02c', '06d', '06h'])

# Full House with 4 irrelevant diamonds
hand_detector(['03d', '03c', '03h', '10d', '10h', '14d', '06d'])

# Pair of 8's King kicker
hand_detector(['08c', '07c', '08s', '10s', '12s', '04c', '13h'])
