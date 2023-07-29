def getNum(): ## Definding number
    num = int(input("Enter the number")) ##input to enter the number
    return num


def getAge(age,num):
    for x in range(num):
     age[x] = int(input("enter age"))


def getTotal(age,num):
                                     #function to calculate total of all ages entered by user.
    t = 0
    for x in range(num):
      t = t + age[x]
      return t                       #main function calling other functions and printing output on console screen.
    
def printAll(age, num, total):
   for x in range(num):
      print(age[x]) 
print("Total = ",total)   
def main():
   n=getNum()   #calling function and storing value returned from it into variable 'n'