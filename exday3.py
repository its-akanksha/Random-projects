# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_name= name1.lower()
second_name = name2.lower()
couple_name = first_name + second_name

true_score=0

for letter in couple_name:
  if letter=="t" or letter=="r" or letter=="u" or letter=="e" in couple_name:
    true_score+=1

love_score=0
for letter in couple_name:
  if letter=="l" or letter=="o" or letter=="v" or letter=="e" in couple_name:
    love_score+=1

t=str(true_score)
l=str(love_score)
final_score=t+l
final_score_as_int = int(final_score)

if final_score_as_int<10 or final_score_as_int>90:
  print(f"Your score is {final_score_as_int}, you go together like coke and mentos.")
elif final_score_as_int>=40 and final_score_as_int<=50:
  print(f"Your score is {final_score_as_int}, you are alright together.")
else:
  print(f"Your score is {final_score_as_int}.")