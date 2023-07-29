## Christopher Gonzalez
## CIT 129
## this program is asking for a user to input invoice information to determine the destination shipping cost
## gathering inforamtion The program is a simple order processing system. It requires the user to enter a 
#valid password before proceeding. It then prompts the user to enter how many orders they want to process, 
#and validates that the number is within the range of 1 to 10. For each order, the program asks the user to 
#provide their name, the total amount of the order, and the shipping destination. The program calculates the 
#shipping cost for each order based on some rules. If the order amount is at least 150, or if the destination is outside 
#of North America, the shipping cost is zero. Otherwise, the shipping cost depends on the destination country. The program 
#prints a summary of each order, including the name, destination, amount and shipping cost.


##this took me about 3 days

## part one 
##Ask for the password. The correct password is 1234.
#If the password is incorrect, ask again until the user enters a correct password.
password = int(input("whats the password :"))
while password != 1234:
    print(" try again incorrect password:  ")
    password = int(input("enter password :"))

## step 2 : Ask for the number of orders to be processed. If this number is 0 or less or more than 10,
## issue an error message and ask again.

count = 0
check = False
shippingDestination = ""
customerName = ""
numberOfOrders = 0
totalAmount = 0
shippingCost = 0


numberOfOrders= int(input("Enter the number of orders you wish to process :  "))
# if numberOfOrders < 0 and numberOfOrders > 11:
while numberOfOrders < 1 or numberOfOrders > 10: 
    print("******* ******** ERROR ***** *********")
    print("Try again must be 1 - 10 assignments")
    numberOfOrders =int (input ("Please enter a valid value between  1-10 : "))
    print("Number of orders: = ", numberOfOrders  )
else: 
    print("You have entered ", numberOfOrders , " number of orders ")
    print("********* ********** ******** order summary ********* ********** ******** ")

while numberOfOrders > count:
    customerName = input("Enter your name: ")
    totalAmount = float(input("What is the total amount : "))
    shippingDestination = input("Enter your destination : " )
    if shippingDestination == "USA" or shippingDestination == "Mexico" or shippingDestination == "Canada":
        check = True
    for i in range(numberOfOrders):
        if shippingDestination == "Mexico" and (totalAmount > 0 and totalAmount < 50):
            shippingCost = 4
        elif shippingDestination == "Canada" and (totalAmount > 0 and totalAmount < 50):
            shippingCost = 8
        elif shippingDestination == "USA" and (totalAmount > 0 and totalAmount < 50):
             shippingCost = 6
        elif shippingDestination == "Mexico" and (totalAmount < 100 and totalAmount >= 50):
            shippingCost = 10
        elif shippingDestination == "Canada" and (totalAmount < 100 and totalAmount >= 50):
         shippingCost = 12
        elif shippingDestination == "USA" and (totalAmount < 100 and totalAmount >= 50):
            shippingCost = 9
        elif shippingDestination == "Mexico" and (totalAmount >= 100 and totalAmount < 150):
            shippingCost = 9
        elif shippingDestination == "Canada" and (totalAmount >= 100 and totalAmount < 150):
            shippingCost = 15
        elif shippingDestination == "USA" and (totalAmount >= 100 and totalAmount < 150):
            shippingCost = 12
        elif (shippingDestination ==  "Mexico" or shippingDestination == "Canada" or shippingDestination == "USA") and (totalAmount >= 150):
            shippingCost = 0
    while check == False:
        shippingDestination = input("Enter your destination : " )
    print("NAME: ",customerName,'\n',
      "Destination : ", shippingDestination,'\n',
      "total Amount : $", format(totalAmount, ".2f"),'\n',
      'Shipping cost : $', shippingCost,".00")    
    count = count + 1

