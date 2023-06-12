print("**********Welcome to the tip calculator**********")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
per = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

totalBill = bill + bill*(per/100)
eachPer = round(totalBill/people, 1)

print("Each person should pay: $",eachPer )