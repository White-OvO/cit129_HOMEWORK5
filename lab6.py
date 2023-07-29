##lab 6


print("Hello world")
##age input

ages = int(input("whats your age :"))
while ages < 18:
    print(" try again you must be atleast 18 ")
    ages = int(input("What is your age :"))
    

##cesius input

celsius = float(input("Enter temperature in Celsius and terminated or 999 to quit: "))


count = 0
total_fahrenheit = 0.0 
total_celsius = 0.0 


while celsius != 999: # loop until the sentinel value is entered
    fahrenheit = (celsius * 9/5) + 32  # convert to Fahrenheit
    print(celsius,"°C ", "is ", fahrenheit, "°F" ) # print the result
    if fahrenheit > 0 and fahrenheit <= 40:
        print("COLD")
    elif fahrenheit > 40 and fahrenheit <= 80:
        print("OKAY")
    else:
        print("HOT")
    count = count + 1
    total_fahrenheit += fahrenheit
    total_celsius += celsius
    celsius = float(input("Enter temperature in Celsius or 999 to quit: ")) # get the next input
  
       
if count > 0:
    average_fahrenheit = total_fahrenheit / count
    average_celsius = total_celsius / count
    print("Average temperature in Fahrenheit: ", format(average_fahrenheit, ".2f"))
    print("Average temperature in Celsius:", format(average_celsius, ".2f"))
else:
    print("No temperatures entered.")    

