import colorama                                                                                                     ## For coloring the output.
from colorama import Fore

def func1():                                                                                                        ## If the choosen mode is a, gets in this function. This function is checking to only inserted number is perfect or not.

    number = int (input ("insert num: "))                                                                           ## User input
    multinumbs = []                                                                                                 ## Array of multipliers list
    for j in range (number-1):                                                                                      ## A for loop for divide process. Range is (number-1) because we don't want to check number/number for finding perfect process. Because number/number has no remainder and mixing the calculation steps up.
        d=number%(j+1)                                                                                              ## Same like above. J is basically 0 if we don't define it. So (j+1) equals 1 in the first step of loop. Every step j increases until reach the number-1. (J+1) = divider. "d" is the mod process.
        if d == 0:                                                                                                  ## If mod process equals to 0 it means no remainder. the Divider is perfect divider.
            print("Number:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
            multinumbs.append(j+1)                                                                                  ## We want this dividers. Added to the list.
        else:                                                                                                       ## If mod process not equals to 0 it means there is a remainder and we don't want this dividers.
            print("Number:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
  
    length = len (multinumbs)                                                                                       ## Gets length of the list's entities.
    multimulti = int(0)                                                                                             ## Defining a variable and make it zero. Because zero is effectless in summation process. 
    print ("exact divisors ", multinumbs)                                                                           ## Printing the members of list before the list getting popped.
    for y in range (length):                                                                                        ## For loop for getting members out of the array and adding into the "multimulti" variable.
        multimulti = multinumbs[-1] + multimulti                                                                    ## Picking and adding process.
        multinumbs.pop()                                                                                            ## Popping last index of array because everytime in the for loop, the loop takes out the last member of the array.
        
    print ("sum of exact divisors:", multimulti)                                                                    ## Printing the  output.
    
    if multimulti == number:                                                                                        ## CHECKER for the EQUALITY!
        print(multimulti, "=", number, Fore.GREEN+"Perfect Number!\n", Fore.WHITE+"Let's Try Again!\n\n")           ## Printing out Perfect.
        main()                                                                                                      ## Goes back to the choosing mode screen.
    else:
        print(multimulti, "≠", number, Fore.RED+"Not Perfect Number\n", Fore.WHITE+"Let's Try Again!\n\n")          ## Printing out Not Perfect.
        main()                                                                                                      ## Goes back to the choosing mode screen.             

    

def func2():
    rangeperfects= []
    multinumbs = []
    number = int (input ("insert num until: "))
    for a in range (number):
        for j in range (number-1):
            d=number%(j+1)
            if d == 0:
                print("Sayı:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
                multinumbs.append(j+1)
            else:
                print("Sayı:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
        number=number-1
  
    print ("exact divisors list: ", multinumbs)
    
    length = len (multinumbs)
    multimulti = int(0)    

    for y in range (length):
        multimulti = multinumbs[-1] + multimulti
        multinumbs.pop()
    print ("sum of exact divisors:", multimulti)
    
    if multimulti == number:
        print(multimulti, "=", number, Fore.GREEN+"Perfect Number!", Fore.WHITE)
        rangeperfects.append(number)
        
        
    elif multimulti != number:
        print(multimulti, "≠", number, Fore.RED+"Not Perfect Number", Fore.WHITE)
        
    
    print(rangeperfects)   
                
        
        
def main():
    option = input("a or b:\n\nTip: c for exit :)\n")
    if option == "a":
        func1()
    elif option== "b":
        func2()    
    elif option== "c":
        quit()      
    else:
        print("please write a, b or c!")
        main()

main()