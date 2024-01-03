import colorama ## For coloring the output.
from colorama import Fore, Back
import time ## For Calculating Elapsed Time
import os ## For clean screen or etc
import sys

def funcA():    ## Slow or fast?
    
    os.system('cls')
    speedmode = input("Slow or Fast?\n\nFor Slow (s), For Fast (f) :)\n\n")
    if speedmode == "s":
        os.system('cls')
        funcANormal()
    elif speedmode == "f":
        os.system('cls')
        funcAFast()    
    else:
        os.system('cls')
        os.system('color 4')
        print("Wrong input!")
        time.sleep(0.5)
        os.system('color 07')
        funcA()
        
def funcANormal():   ## If the choosen mode is a, gets in this function. This function is checking to only inserted number is perfect or not. Normal mode.
    number = int (input ("insert num: ")) ## User input
    multinumbs = [] ## Array of multipliers list
    start = time.time()
    for j in range (number-1):  ## A for loop for divide process. Range is (number-1) because we don't want to check number/number for finding perfect process. Because number/number has no remainder and mixing the calculation steps up.
        d=number%(j+1)  ## Same like above. J is basically 0 if we don't define it. So (j+1) equals 1 in the first step of loop. Every step j increases until reach the number-1. (J+1) = divider. "d" is the mod process.
        if d == 0:  ## If mod process equals to 0 it means no remainder. the Divider is perfect divider.
            print("Number:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
            multinumbs.append(j+1)  ## We want this dividers. Added to the list.
        else:   ## If mod process not equals to 0 it means there is a remainder and we don't want this dividers.
            print("Number:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
  
    length = len (multinumbs)   ## Gets length of the list's entities.
    multimulti = int(0) ## Defining a variable and make it zero. Because zero is effectless in summation process. 
    print ("\nexact divisors ", multinumbs)   ## Printing the members of list before the list getting popped.
    for y in range (length):    ## For loop for getting members out of the array and adding into the "multimulti" variable.
        multimulti = multinumbs[-1] + multimulti    ## Picking and adding process.
        multinumbs.pop()    ## Popping last index of array because everytime in the for loop, the loop takes out the last member of the array.
        
    print ("\nsum of exact divisors:", multimulti)    ## Printing the  output.
    end = time.time()
    print("\nTime Elapsed:", end - start)
    if multimulti == number:    ## CHECKER for the EQUALITY!
        print("\n", Back.LIGHTBLUE_EX, multimulti, "=", number, Back.BLACK, Fore.GREEN+"\t\tPerfect Number!", Fore.WHITE+"\n\nTry Again?\n")    ## Printing out Perfect.
        tagain = input("(y/n)?\t-\t")
        match tagain:
            case "y":
                start = 0
                end = 0
                os.system('cls')
                main()  ## Goes back to the choosing mode screen. 
            case "n":
                return(exit)
    else:
        print("\n", Back.LIGHTBLUE_EX,multimulti, "≠", number, Back.BLACK, Fore.RED+"\t\tNot Perfect Number", Fore.WHITE+"\n\nTry Again?\n")   ## Printing out Not Perfect.
        tagain = input("(y/n)?\t-\t")
        match tagain:
            case "y":
                start = 0
                end = 0
                os.system('cls')
                main()  ## Goes back to the choosing mode screen. 
            case "n":
                return(exit)             
    
def funcAFast():    ## If the choosen mode is a, gets in this function. This function is checking to only inserted number is perfect or not. Fast mode.

    number = int (input ("insert num: ")) ## User input
    multinumbs = [] ## Array of multipliers list
    start = time.time()
    for j in range (number-1):  ## A for loop for divide process. Range is (number-1) because we don't want to check number/number for finding perfect process. Because number/number has no remainder and mixing the calculation steps up.
        d=number%(j+1)  ## Same like above. J is basically 0 if we don't define it. So (j+1) equals 1 in the first step of loop. Every step j increases until reach the number-1. (J+1) = divider. "d" is the mod process.
        if d == 0:  ## If mod process equals to 0 it means no remainder. the Divider is perfect divider.
            multinumbs.append(j+1)  ## We want this dividers. Added to the list.
       
    length = len (multinumbs)   ## Gets length of the list's entities.
    multimulti = int(0) ## Defining a variable and make it zero. Because zero is effectless in summation process. 
    print ("\nexact divisors ", multinumbs) ## Printing the members of list before the list getting popped.
    for y in range (length):    ## For loop for getting members out of the array and adding into the "multimulti" variable.
        multimulti = multinumbs[-1] + multimulti    ## Picking and adding process.
        multinumbs.pop()    ## Popping last index of array because everytime in the for loop, the loop takes out the last member of the array.
        
    print ("\nsum of exact divisors:", multimulti)  ## Printing the  output.
    end = time.time()
    print("\nTime Elapsed:", end - start)
    if multimulti == number:    ## CHECKER for the EQUALITY!
        print("\n", Back.LIGHTBLUE_EX, multimulti, "=", number, Back.BLACK, Fore.GREEN+"\t\tPerfect Number!", Fore.WHITE+"\n\n Try Again?\n")   ## Printing out Perfect.
        tagain = input("(y/n)?\t-\t")
        match tagain:
            case "y":
                start = 0
                end = 0
                os.system('cls')
                main()  ## Goes back to the choosing mode screen. 
            case "n":
                return(exit)
    else:        
        print("\n", Back.LIGHTBLUE_EX, multimulti, "≠", number, Back.BLACK, Fore.RED+"\t\tNot Perfect Number", Fore.WHITE+"\n\nTry Again?\n")   ## Printing out Not Perfect.
        tagain = input("(y/n)?\t-\t")
        match tagain:
            case "y":
                start = 0
                end = 0
                os.system('cls')
                main()  ## Goes back to the choosing mode screen. 
            case "n":
                return(exit)
global perf
perf = rangeperfects= []  

def funcB():
    os.system("cls")
    speedmode = input("Slow or Fast?\n\nFor Slow (s), For Fast (f) :)\n\n")
    if speedmode == "s":
        os.system('cls')
        number = int (input ("Insert num until: "))
        if number > 40000:
            os.system('cls')
            os.system('color 4')
            print("The limit in this mode is 40000! Please insert lower number.")
            time.sleep(1)
            os.system('color 07')
            funcB()
        else:
            funcBNormal(number)
            os.system("cls")

    elif speedmode == "f":
        os.system("cls")
        number = int (input ("Insert num until: "))
        if number > 40000:
            os.system('cls')
            os.system('color 4')
            print("The limit in this mode is 40000! Please insert lower number.")
            time.sleep(1)
            os.system('color 07')
            funcB()
        else:
            funcBFast(number)
            os.system("cls")
    
    else:
        os.system('cls')
        os.system('color 4')
        print("Wrong input!")
        time.sleep(0.5)
        os.system('color 07')
        funcB()
    
def funcBNormal(number):
    
    multinumbs = []
    if number > 1:       
        for j in range (number-1):
            d=number%(j+1)
            if d == 0:
                print("Sayı:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
                multinumbs.append(j+1)
            else:
                print("Sayı:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
  
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
            funcBNormal(number-1)
            
        elif multimulti != number:
            print(multimulti, "≠", number, Fore.RED+"Not Perfect Number", Fore.WHITE)
            funcBNormal(number-1)
        else:
            print("Something Wrong?")
    elif number == 1:
        print("\n", Back.LIGHTBLUE_EX, rangeperfects, Back.BLACK, "\n\nTry Again?\n")
        tagain = input("(y/n)?\t-\t")
        match tagain:
            case "y":
                start = 0
                end = 0
                os.system('cls')
                main()  ## Goes back to the choosing mode screen. 
            case "n":
                return(exit)
    else:
        print("?")
 
def funcBFast(number):
    
    multinumbs = []
    if number > 1:       
        for j in range (number-1):
            d=number%(j+1)
            if d == 0:
                multinumbs.append(j+1)
        length = len (multinumbs)
        multimulti = int(0)   
        for y in range (length):   
            multimulti = multinumbs[-1] + multimulti
            multinumbs.pop()          
        if multimulti == number:
            rangeperfects.append(number)
            funcBFast(number-1)          
        elif multimulti != number:
            funcBFast(number-1)
        else:
            print("Something Wrong?")
    elif number == 1:
        print("\n", Back.LIGHTBLUE_EX, rangeperfects, Back.BLACK, "\n\nTry Again?\n")
        tagain = input("(y/n)?\t-\t")
        match tagain:
            case "y":
                start = 0
                end = 0
                os.system('cls')
                main()  ## Goes back to the choosing mode screen. 
            case "n":
                return(exit)
    else:
        print("?")
    
def main():
    os.system("cls")
    sys.setrecursionlimit(155000)
    option = input("a or b:\n\nTip: c for exit :)\n\n")
    if option == "a" or option == "A":
        funcA()
    elif option == "b" or option == "B":
        rangeperfects.clear()
        funcB()    
    elif option == "c" or option == "C":
        quit()
    elif option == "d":
        print(sys.getrecursionlimit())
    else:
        os.system('cls')
        os.system('color 4')
        print("Wrong input!")
        time.sleep(0.5)
        os.system('color 07')
        main()

main()