# Poker Simulator

This repository is in development with the overall goal of inputting opponents' hands or range of hands, as well as my own hand, and outputting a probability of winning.

## Definitions
### Hand Rankings
1. Straight Flush
2. Four of a Kind
3. Full House
4. Flush
5. Straight
6. Three of a Kind
7. Two Pair
8. Pair
9. High Card

## One_hand.py

Hand_detector: Detect the value of a hand
- Input: List of 7 cards in a person's hand after the river (two pocket cards and five community cards)
- Output: Tuple where the first value is the rank of the hand (1-9) and second is the five cards in the player's hand

## One_hand_test.py

Creates all test examples for hand_detector in one_hand.py to ensure correctness.
