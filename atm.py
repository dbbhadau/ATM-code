# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:16:52 2019

@author: Disha Bhadauria
"""

print("welcom to bank atm")
restart=('Y') #tuple x=('a','b'),x=(1,2,3)
chances =3 # 3 chances for correct atm pin
bal= 67.14

while chances>=0:
    pin=int(input("enter pin"))
    if pin==(1234):
        print("pin correct")
        while restart not in ('n','No','no','n'):
            print(" 1 for bal")
            print(" 2 for withdraw")
            print(" 3 for pay in")
            print(" 4 for return card")
            option = int(input("enter option number"))
            if option==1:
                print("bal is ",bal)
                restart =input("would you like to go back?")
                if restart in ('n','No','no','n'):
                    print("Thank you")
                    break
            elif option==2:
                option2=('y')
                withdraw=float(input("how much withdraw "))
                if withdraw in [10,20,40,60,80,100]:
                    bal=bal-withdraw
                    print("new bal",bal)
                    restart =input("would you like to go back?")
                if restart in ('n','No','no','n'):
                    print("Thank you")
                    break
                elif withdraw not in [10,20,40,60,80,100]: 
                    print("invalid amt ")
                    restart =('y')
                elif withdraw == 1:
                    withdraw=float(input("how much withdraw "))
            elif option==3:
                pay_in=float(input("how much pay_in "))
                bal=bal+pay_in
                print("new bal",bal)
                restart =input("would you like to go back?")
                if restart in ('n','No','no','n'):
                    print("Thank you")
                    break
            elif option ==4:
                print ("wait for card to be returned")
                print("Thank you")
                break
            else:
                print("enter correct option number")
                restart=('y')
    elif  pin !=(1234):
        print("wrong pin")
        chances=chances-1
        if chances==0:
            print("no more tries")
            break
                
                    
                