# File Name: dinner.py
# Author Name: Sivaramchandar Suresh
# Date: Wednesday, February 8, 2023
# The purpose of this program is to demonstrate my knowledge of using for loops, decision operators, expressions,
# functions, strings and user input to deliver food to the customer based on their dietary preference in the order.

# TAXRATE is a constant which is set to 0.13.
TAXRATE= 0.13

# Variables numberOfInviteesOrderedPizza, numberOfInviteesOrderedPasta, numberOfInviteesOrderedFalafel,
# numberOfInviteesOrderedSteak and numberOfInviteesOrderedBeverage are initialized to 0.
numberOfInviteesOrderedPizza= numberOfInviteesOrderedPasta= numberOfInviteesOrderedFalafel=numberOfInviteesOrderedSteak= numberOfInviteesOrderedBeverage= 0
numberOfInvitees= int(input("Please enter the number of invitees:"))

# Variables costOfPizza, costOfPasta, costOfFalafel, costOfSteak and costOfBeverage are initialized to 0.00.
costOfPizza= costOfPasta= costOfFalafel= costOfSteak= costOfBeverage= 0.00

# This for loop is executed a number of times based on the value that the user enters for the variable name
# numberOfInvitees.
for i in range(numberOfInvitees):
    print("Please enter the order details for invitee Number %d/%d"%(i+1, numberOfInvitees))
    answerForKetoFriendlyMeal= input("Do you want a keto friendly meal?")
    answerForVeganMeal= input("Do you want a vegan meal?")
    answerForGlutenFreeMeal= input("Do you want a Gluten-free meal?")

    if answerForKetoFriendlyMeal== "y" and answerForVeganMeal=="y" and answerForGlutenFreeMeal!= "y":
        numberOfInviteesOrderedPizza+= 1
        costOfPizza+= 44.50
    elif answerForKetoFriendlyMeal!= "y" and answerForVeganMeal=="y" and answerForGlutenFreeMeal!="y":
        numberOfInviteesOrderedPasta+= 1
        costOfPasta+= 48.99
    elif answerForKetoFriendlyMeal== "y" and answerForVeganMeal== "y" and answerForGlutenFreeMeal== "y":
       numberOfInviteesOrderedFalafel+= 1
       costOfFalafel+= 52.99
    elif answerForKetoFriendlyMeal== "y" and answerForVeganMeal!= "y" and answerForGlutenFreeMeal== "y":
        numberOfInviteesOrderedSteak+= 1
        costOfSteak+= 49.60
    else:
        numberOfInviteesOrderedBeverage+= 1
        costOfBeverage+= 5.99
percentageTip= int(input("How much do you want to tip your server (% percent)?"))

# Below this line, the code prints or displays the numberOfInviteesOrderedPizza, numberOfInviteesOrderedPasta,
# numberOfInviteesOrderedFalafel, numberOfInviteesOrderedSteak, numberOfInviteesOrderedBeverage. It also displays,the
# values for the costOfPizza, costOfPasta, costOfFalafel and costOfBeverage.
print("You have %d invitees with the following orders:"%numberOfInvitees)
print("%d invitees ordered Pizza. The cost is: $%.2f "%(numberOfInviteesOrderedPizza, costOfPizza))
print("%d invitees ordered Pasta. The cost is: $%.2f "%(numberOfInviteesOrderedPasta, costOfPasta))
print("%d invitees ordered Falafel. The cost is: $%.2f "%(numberOfInviteesOrderedFalafel, costOfFalafel))
print("%d invitees ordered Steak. The cost is: $%.2f"
      %(numberOfInviteesOrderedSteak, costOfSteak))
print("%d invitees ordered only beverage. The cost is: $%.2f "%(numberOfInviteesOrderedBeverage, costOfBeverage))
totalCostBeforeTax= costOfPizza + costOfPasta + costOfFalafel + costOfSteak + costOfBeverage
print("The total cost before tax is $%.2f"%totalCostBeforeTax)
totalCostAfterTax= totalCostBeforeTax * TAXRATE + totalCostBeforeTax
print("The total cost after tax is $%.2f"%(totalCostAfterTax))
totalCostAfterTip= totalCostAfterTax*((100 + percentageTip)/100)
print("The total cost after %d%% tip is $%d"%(percentageTip, round(totalCostAfterTip)))
