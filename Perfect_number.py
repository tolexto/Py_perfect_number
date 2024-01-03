from ast import Constant
import colorama
from colorama import Fore, Back, Style

def func1():

    number = int (input ("insert num: "))
    multinumbs = []
    for j in range (number-1):
        d=number%(j+1)
        if d == 0:
            print("Number:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
            multinumbs.append(j+1)
        else:
            print("Number:", number, "\tDivider:", j+1,"\tRemainder:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
  
    length = len (multinumbs)
    multimulti = int(0)
    print ("exact divisors ", multinumbs)
    for y in range (length):
        multimulti = multinumbs[-1] + multimulti
        multinumbs.pop()
        
    print ("sum of exact divisors:", multimulti)
    
    if multimulti == number:
        print(multimulti, "=", number, Fore.GREEN+"Perfect Number!\n", Fore.WHITE+"Let's Try Again!\n\n")
        main()
    else:
        print(multimulti, "≠", number, Fore.RED+"Not Perfect Bro\n", Fore.WHITE+"Let's Try Again!\n\n")
        main()

    

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
        print(multimulti, "≠", number, Fore.RED+"Not Perfect Bro", Fore.WHITE)
        
    
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