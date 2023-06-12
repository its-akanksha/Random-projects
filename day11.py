
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

play_decision = input("Do you want to play a game of blackjack? 'Y' or 'N': ").lower()

if play_decision=='y':
  play=True

if play_decision == 'n':
  play = False
# else:
#   print("Please print a valid input")
#   quit()

from art11 import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# print(player_cards, comp_cards)

def if_computer_blackjack(pc,cc):

  if 10 and 11 in cc:
  #   print(f"    Your final cards: {pc}, Final score: {sum(pc)}")
  # print(f"    Computer's final cards: {cc}, Computer's final score: {sum(cc)}")
    return "Computer gets a blackjack. Total score of computer is 21. Computer wins!"

  if 10 and 11 in pc:
  #   print(f"    Your final cards: {pc}, Final score: {sum(pc)}")
  # print(f"    Computer's final cards: {cc}, Computer's final score: {sum(cc)}")
    return "Player gets a blackjack. Total score of player is 21. Player wins!"

def ace_case(hand):
  if 11 in hand and sum(hand)>21:
      for i in range(len(hand-1)):
          if hand[i]==11:
              hand[i]=1
      return sum(hand)

def computer_hand(cc, cards):
  while sum(cc)<=16:
    cc.append(random.choice(cards))

def another_card_for_player(pc, cards):
  pc.append(random.choice(cards))
  print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
  print(f"    Computer's first card: {comp_cards[0]}")

while play is True:
    ## Assign cards to the players
    player_cards = [random.choice(cards), random.choice(cards)]
    comp_cards = [random.choice(cards), random.choice(cards)]

    ##Showing the player their and computer's cards
    print(f"    Your cards: {player_cards}, Current score: {sum(player_cards)}")
    print(f"    Computer's first card: {comp_cards[0]}")

    ##Asking if they want another card
    to_cont=True

    while to_cont is True:
        another_card_player = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card_player =='y' and sum(player_cards)<22:
          another_card_for_player(player_cards, cards)
          if sum(player_cards)>=22:
              ace_case(player_cards)
              # print(f"    Your final hand: {player_cards}, final score = {sum(player_cards)}")
              # print(f"    Computer's final hand: {comp_cards}, final score = {sum(comp_cards)}")
              to_cont = False
        else:
          to_cont =False

    computer_hand(comp_cards, cards)
    if_computer_blackjack(player_cards, comp_cards)
    ace_case(comp_cards)

    print(f"    Your final hand: {player_cards}, final score = {sum(player_cards)}")
    print(f"    Computer's final hand: {comp_cards}, final score = {sum(comp_cards)}")

    if sum(player_cards)>sum(comp_cards) and sum(player_cards)<22:
        print("You win!")
    if sum(comp_cards)>sum(player_cards) and sum(comp_cards)<22:
        print("You lose!")
    if sum(comp_cards)==sum(player_cards):
        print("It's a draw!")
    if sum(comp_cards)>=22 and sum(player_cards)<22:
        print("Opponent went over. You win!")
    if sum(player_cards)>=22 and sum(comp_cards)<22:
        print("You went over. You lose")
      # else:
      #   print("It's a draw")

    new_game = input("Do you want to play a game of blackjack? 'Y' or 'N': ").lower()

    if new_game == 'n':
        play=False
