## Christopher Gonzalez
## cit129
## lab 7 
## 





# Enter the number of temperature readings: -1
# Invalid - Enter the number of temperature readings: 55 Invalid - Enter the number of temperature readings:3 Enter temperature in degrees Celsius: -102
# Invalid - Enter temperature in degrees Celsius: 110 Invalid - Enter temperature in degrees Celsius: 50 Degrees in Fahrenheit = 122.00
# count = 0

# fahrenheit = 0

# count = 0

# fahrenheit = int(input("Enther tempature : "))

# while fahrenheit < 100 and fahrenheit > -100 and 
#     celsius = (fahrenheit * 9/5) + 32
   
#     count = count + 1
# else:
#     fahrenheit = int(input("input a number from -100 through 100 ,nther tempature : "))
#     celsius = (fahrenheit * 9/5) + 32
#     count = count + 11
   
1
# print (fahrenheit, " = ", celsius)

## converting farhenheit to celsius

########################################### first attemot ##############################################################
# count = 0

# fahrenheit = int(input("Enter temperature: "))

# while fahrenheit < 100 and fahrenheit > -100:
#     celsius = (fahrenheit * 9/5) + 32 # This is the correct formula to convert from Fahrenheit to Celsius
#     count = count + 1
#     print(fahrenheit, " = ", celsius)
#     fahrenheit = int(input("Enter temperature: "))
# else : fahrenheit = int(input("Enter temperature: ")):
#     celsius = (fahrenheit * 9/5) + 32 # This is the correct formula to convert from Fahrenheit to Celsius
#     count = count + 1
#     print(fahrenheit, " = ", celsius)
#     fahrenheit = int(input("Enter temperature: "))



########################################### second attemot ##############################################################

# count = 0

# fahrenheit = int(input("Enter temperature: "))




# while fahrenheit < 100 and fahrenheit > -100:
#     celsius = (fahrenheit * 9/5) + 32 # This is the correct formula to convert from Fahrenheit to Celsius
#     count = count + 1
#     print(fahrenheit, " = ", celsius)
#     fahrenheit = int(input("Enter temperature: "))
# else:fahrenheit < 100 and fahrenheit > -100
# fahrenheit = int(input("Enter temperature: "))
# celsius = (fahrenheit * 9/5) + 32
# count = count + 11
# print(fahrenheit, " = ", celsius)




########################################### third attemot ##############################################################


Fahrenheit = 0 
Celsius = 0
count = 0 
total_fahrenheit = 0.0 
total_celsius = 0.0 



## wrong way to put it:::::::::::::
# temperature = int(input("Enter Celsius: "))
# while temperature < -100 and temperature > 100:
#         print("MUST BE between -100 and 100 try again  :")
#         temperature = int(input("Enter Celsius: "))


#########Wrong formula for faregeit 
##Fahrenheit = (9 /5) Celsius + 32

## Calculate and display the average temperature in degrees Fahrenheit and Celsius.

print("wanna play a game ")
count = 0 
total_celsius = 0
total_fahrenheit = 0




celsius = int(input("Enter any number to see a converstion of Celsius to farenheit: "))

while count < 3:
    while celsius < -100 or celsius > 100:
        print("The temperature must be between -100 and 100 degrees Celsius. Try again:")
    celsius = int(input("Enter Celsius: "))
    ##count > 3: # loop until the sentinel value is entered
    fahrenheit = (celsius * 9/5) + 32   # convert to Fahrenheit
    print(celsius,"°C ", "is ", fahrenheit, "°F" ) # print the result
    if fahrenheit > 0 and fahrenheit <= 40:
        print("COLD")
    elif fahrenheit > 40 and fahrenheit <= 80:
        print("OKAY")
    else:
        print("HOT")
 
    total_fahrenheit += fahrenheit
    total_celsius += celsius
    count = count + 1
    average_fahrenheit = total_fahrenheit / count
    average_celsius = total_celsius / count

 
    if count > 3:print("Average temperature in Fahrenheit: ", format(average_fahrenheit, ".2f"))
print("Average temperature in Celsius:", format(average_celsius, ".2f"))
print("Average temperature in Fahrenheit: ", format(average_fahrenheit, ".2f"))