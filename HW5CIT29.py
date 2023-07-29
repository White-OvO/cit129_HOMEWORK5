print("Hello world")


## the number of rooms booked
## the coar od renring one room
## THE YUMBER OF DAYS THE TOOMS ARE BOOKE\





dayDiscount = 0.0 ##additionalDiscount
discount = 0.0
numOfDays = 0 
numberOfRooms = 0
costOfRoom = 0   ##rent cost
salesTaxs = 0




## number of rooms booked
numberOfRooms= int(input("Enter the number of rooms you wish to book: "))
while numberOfRooms < 0:
    print("issue an error message and do not perform any calculation nor produce any other output.")

    

print("Thank you , you want have selected: ", numberOfRooms, " number of rooms")

while numberOfRooms < 1:
    print ("*********ERROR*******  You must select at least a single room.")
    numberOfRooms =int ( input("Please enter again:"))


## price of cost per room
costOfRoom = float(input("How much does each room cost a night ? " ))
print("You have enetered the amount of ", " $" ,costOfRoom , " per room")



## number of days the rooms are going to be booked
numOfDays = int(input("How many days  do wish to reserve : "))
print("You have selected to reserve for ", numOfDays, "Days")


amountBeforeTaxs =(numberOfRooms * costOfRoom* numOfDays ) 



if numOfDays > 3:
    print("Qualification: 5% discount")
    dayDiscount = .05

if numberOfRooms < 10 > 0:
    discount = .1
    print("qualified: 10% discount")

## numner of tooms booked is betwee 10 and 20
if numberOfRooms > 10 < 20:
    discount = .2
    print("Qualified: 20 % discount")

## number of rooms book is greater tham 2-
if numberOfRooms > 20:
    discount = .3
    print("The number of rooms is greater than 20 there for here is ", discount, "% Discount")



## sale taxes

salesTaxs = float(input("Enter the sale taxes for transactions in percent ")) 
print("Sales taxes for transaction is : $ ",salesTaxs )



##### along line 133
##saleTaxesPercentage = salesTaxs / 100 + 1

totalDiscount = amountBeforeTaxs * discount 

totalAmountAfterDiscount =  amountBeforeTaxs - totalDiscount

##
# 
# 
# totalBill= totalAmountAfterDiscount * (salesTaxs)
##
# 
# 
# 
# 
#  discount - tax

##totalCost = amountBeforeTaxs - discount
totalCost = amountBeforeTaxs - (amountBeforeTaxs * discount)


########################## total cost 
###########################totalPreTax = totalCost - (totalCost ) * discount

##f the number of rooms booked is between 1 and 10, the discount is 10%; more than 10, but less than or equal to 20, the discount is 20%; and more than 20 rooms, the discount is 30%.
# If rooms are booked for at least 3 days, then there is an additional 5% discount.
# If number of rooms booked is 0 or less, issue an error message and do not perform any calculation nor produce any other output.##



#If rooms are booked for at least 3 days, then there is an additional 5% discount.
#If number of rooms booked is 0 or less, issue an error message and do not perform any calculation nor produce any other output.




## if the number of tooms booked is between 1 and 10




## part 2 

#  The cost of renting one room,
# • The discount on each room as a percent,
# • The discount based on number of days as a percent,
# • The number of rooms booked,
# • The number of days the rooms are booked,
# • The total cost of the rooms before tax,
# • The sales tax (calculated based on total bill before any discounts), and • The total billing amount.

print("*****Summary report  ******")


print("the cost of renting one room is : $", costOfRoom)
print("The total disocunt on each room is ", discount * 100, "%")
print("additional discount if applied :", dayDiscount , "%")
print("number of rooms booked : ", numberOfRooms)
print("Number of Days Booked:",numOfDays,"days" )

print("Total cost :$", totalAmountAfterDiscount)


# totalCostBeforeTax=numberOfRooms*costOfRoom+dayDiscount*(numOfDays/
# 7)*discount*((numberOfRooms)/48)*(numberOfRooms>6)+(numberOfRooms<=6)*
##tax = salesTaxs *  amountBeforeTaxs


##### along line 77
# print("TAX : $",format(saleTaxesPercentage, ".2f"))
##print("amount with sale tax or GrandTotal:  ", tax)


##wrong
##print("Tax: ",(saleTaxesPercentage / 100) * (totalAmountAfterDiscount))
##ans: 10.44
totalBill = amountBeforeTaxs
totalTax = totalBill * (salesTaxs * .01)
print("tax : ", totalTax)
print("ddddddddddddddd")

##print ("Total amount", totalAmount)

totalBill = amountBeforeTaxs
print("Total bill ", totalCost + totalTax)



