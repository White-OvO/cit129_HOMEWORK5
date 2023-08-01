##chritopher gonzalez
## cit 129
## homework 7
## NOTE THIS PROGRAM has FUNCTIONS  this program outputs "ACME " 3X and then 1 through 9 skipping 2 returninga number of products sold
## validates the input to its value 1 - 1000 and returns a validated number, by having a input to the functions of products and sets the 
## discounut percentage , later outputing the total results of the total order



##function 1 
def function1():
    chris ="Christopher Gonzalez"

    print(chris)
    count = 0
    while count < 3:
        print("ACME Company ")
        count =  count + 1  
    for i in range(1, 10, 2):
        print(i)

## function 2
# A function that returns the number of products sold. The function prompts the user for the number of products, validates the input to assure it’s a 
# value between 1 and 1000 (inclusive), and return the validated number. The function does not have a parameter and returns a value.
def sales():  
    # Get the user input for the number of products
    productsSold = int(input("Enter the number of product sold : "))
    # Validate the input using a while loop
    while productsSold < 1 or productsSold > 1000:
        print("The number of products must be between 1 and 1000")
        productsSold = int(input("Enter the number of product sold : "))   
    # Return the validated number
    return productsSold

# function 3
#Function 3: This function accepts the number of products sold as its parameter. For each product, ask for the quantity and the unit cost of the product and set the discount percentage according to the following table: 
# NOTE: This function accepts the number of products sold as its parameter and calculates and prints the required data. It does not return a value.

# totalProductSold = 0
# discount = 0 
# quantity = 0
# totalQuantity = 0
# grandTotal = 0

# def soldproduct:
def soldproduct(productsSold):
    # Initialize the variables
    totalProductSold = 0
    discount = 0 
    quantity = 0
    totalQuantity = 0
    grandTotal = 0
    # Loop until all products are sold
    while totalProductSold < productsSold: 
        # Get the user input for quantity and unit cost
        quantity = int(input("Enter the total quanity for this order : "))
        unitCost = float(input("what is the total unit cost price : $"))
        print("*************** summary ******************************")   
        print("quanity of ", quantity ,"\n", "Unit Cost: ", unitCost,"\n")
        # Increment the total product sold
        totalProductSold += 1
        # Determine the discount based on the quantity
        if quantity < 19 and quantity > 1:
            discount = 20
        elif quantity >= 20 and quantity <= 49:
            discount = 30
        elif quantity >= 50 and quantity <= 99:
            discount = 40
        elif quantity >= 100:    
          discount = 50
        # Calculate the price before discount, the amount of discount and the final cost
        priceBeforeDiscount = (quantity * unitCost )
        print("price before discount = :", priceBeforeDiscount)
        print("The total amount of discount : ", discount,"%")
        amountOfDiscount = (priceBeforeDiscount * (discount / 100))
        print("Amount of discount : ",amountOfDiscount )

        amountOfDiscount = (priceBeforeDiscount * discount) / 100
        # Update the total quantity and grand total
        totalQuantity += quantity
        grandTotal += priceBeforeDiscount - amountOfDiscount
        print(f"Final cost after discount : $ {priceBeforeDiscount - amountOfDiscount:.2f}")
###) Accumulate the grand total of quantities sold
    print("******** F I N A L R E P O R T ****************************" )
    TotalOfQuantities = quantity * productsSold

    print(f"The total number of quantities is {totalQuantity}")
    print(f"Grand total of all products: ${grandTotal:.2f}")
##print("Grand total of quantities sold : ", grandTotalOfQuantities)

# Call function 1
function1()

# Call function 2 and store the return value in a variable
productsSold = sales()

# Call function 3 and pass the variable as an argument
soldproduct(productsSold)
