## Christopher Gonzalez
## cit129
## lab 7 
## this program is a temapature reader for three inputs with the 
## output of a average othis code is a tempature recorder, with the input of tempature in celsius the program than converts to fareneheit and than outputs the toal average tempature for both the celsius and fahrenheit





Fahrenheit = 0 
Celsius = 0
count = 0 
total_fahrenheit = 0.0 
total_celsius = 0.0 



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