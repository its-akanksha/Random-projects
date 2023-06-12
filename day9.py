from replit import clear
from day9Art import logo

biddings={}
to_continue_or_not = True


while to_continue_or_not is True:
  print(logo)
  name = input("Please tell your name: ")
  amt = int(input("Please tell the amount that you would like to bid: $"))
  next_person=input("Type 'yes' if there is another player and 'no' if there is not: ").lower()
  if next_person=="no":
    to_continue_or_not = False
  else:
    clear()
  biddings.update({name:amt})

biggest_val = 0

for key,value in biddings.items():
  if value>biggest_val:
    biggest_val = value

print("The highest bidder is: ", list(biddings.keys())[list(biddings.values()).index(biggest_val)])
