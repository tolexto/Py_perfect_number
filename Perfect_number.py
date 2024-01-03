import colorama
from colorama import Fore, Back, Style

def func1():

    number = int (input ("insert num: "))
    multinumbs = []
    for j in range (number-1):
        d=number%(j+1)
        if d == 0:
            print("Sayı:", number, "\tBölen:", j+1,"\tKalan:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
            multinumbs.append(j+1)
        else:
            print("Sayı:", number, "\tBölen:", j+1,"\tKalan:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
  
    print ("Tam bölenler list: ", multinumbs)
    length = len (multinumbs)
    multimulti = int(0)    

    for y in range (length):
        multimulti = multinumbs[-1] + multimulti
        multinumbs.pop()
    
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
                print("Sayı:", number, "\tBölen:", j+1,"\tKalan:", d, Fore.GREEN+"\tSuccess!", Fore.WHITE)
                multinumbs.append(j+1)
            else:
                print("Sayı:", number, "\tBölen:", j+1,"\tKalan:", d, Fore.RED+"\tNot Success!", Fore.WHITE)
        number=number-1
  
    print ("Tam bölenler list: ", multinumbs)
    
    length = len (multinumbs)
    multimulti = int(0)    

    for y in range (length):
        multimulti = multinumbs[-1] + multimulti
        multinumbs.pop()
    
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