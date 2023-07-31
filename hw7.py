#A function that displays your own full name, use a loop to display the message “ACME Company” 3 times, and the numbers 1 through 9 with steps of 2. This function does not have any parameters and does not return a value.

##function 1 
fullName = chirs =("Christopher Gonzalez")

print(chirs)
count = 0
while count < 3:
    print("ACME Company ")
    count =  count + 1  
for i in range(1, 10, 2):
    print(i)




## function 2
# A function that returns the number of products sold. The function prompts the user for the number of products, validates the input to assure it’s a 
# value between 1 and 1000 (inclusive), and return the validated number. The function does not have a parameter and returns a value.

productsSold = int(input("Enter the number of product sold : "))
if productsSold < 1000 and productsSold > 1: 
    print(productsSold , "= total sales of products")
else:
    productsSold = int(input("must be between 1 and 10000Enter the number of product sold : "))   


# function 3
#Function 3: This function accepts the number of products sold as its parameter. For each product, ask for the quantity and the unit cost of the product and set the discount percentage according to the following table: 
# NOTE: This function accepts the number of products sold as its parameter and calculates and prints the required data. It does not return a value.

totalProductSold = 0
discount = 0 
quantity = 0
totalQuantity = 0
grandTotal = 0


while productsSold > totalProductSold: 
    quantity = int(input("Enter the total quanity for this order : "))
    unitCost = float(input("what is the total unit cost price : $"))
    print("*************** summary ******************************")   
    print("quanity of ", quantity ,"\n", "Unit Cost: ", unitCost,"\n")
    totalProductSold = totalProductSold + 1
    if quantity < 19 and quantity > 1:
        discount = 20
    elif quantity >= 20 and quantity <= 49:
        discount = 30
    elif quantity >= 50 and quantity <= 99:
        discount = 40
    elif quantity >= 100:    
      discount = 50
    priceBeforeDiscount = (quantity * unitCost )
    print("price before discount = :", priceBeforeDiscount)
    print("The total amount of discount : ", discount,"%")
    amountOfDiscount = (priceBeforeDiscount * (discount / 100))
    print("Amount of discount : ",amountOfDiscount )

    amountOfDiscount = (priceBeforeDiscount * discount) / 100
    totalQuantity += quantity
    grandTotal += priceBeforeDiscount - amountOfDiscount
    print(f"Final cost after discount : $ {priceBeforeDiscount - amountOfDiscount:.2f}")
###) Accumulate the grand total of quantities sold
print("******** F I N A L R E P O R T ****************************" )
TotalOfQuantities = quantity * productsSold

print(f"The total number of quantities is {totalQuantity}")
print(f"Grand total of all products: ${grandTotal:.2f}")
##print("Grand total of quantities sold : ", grandTotalOfQuantities)



  