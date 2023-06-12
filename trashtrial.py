def ace_case(hand):
  if 11 in hand and sum(hand)>2:
    hand[0]=1
    return sum(hand)

comp_cards = [11, 9, 10]
res = ace_case(comp_cards)

print(res)
