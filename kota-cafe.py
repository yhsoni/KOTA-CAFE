import chai
import coffee
import snacks
import coldd

print("_____________**************Welcome To Kota-Cafe**************_____________")
print("     \n")
print("--------------------------!!!what you like to have!!!--------------------------")

w="y"
while(w=="y"):
    print("press:-")
    print("0 for Chai\n"
          "1 For Coffee\n"
          "2 For Snacks\n"
          "3 For Cold Drinks\n"
          "4 For Water Bottle\n")


    menu = int(input("Enter Your Choice:-"))
    if(menu == 0):
        print(" ")
        print("Plese Select Chai Flav.")    
        ch=chai.chai()
          
    if(menu == 1):
        print(" ")
        print("Plese Select Coffee Flov.")
        co=coffee.coffee()
    
    if(menu == 2):
        print(" ")
        print("Plese Select Snacks :-")
        sn=snacks.snacks()
    
    if(menu == 3):
        print(" ")
        print("Plese Select Cold Drinks")
        coldd.cold()

    if(menu == 4):
        print(" ")
        print("Plese Select Water Bottle:-\n"
              "A for 1 liter = 20RS\n"
              "B for 500ml   = 10RS\n")
        water=input()
        if(water=='a'):
            w=print("Total = 20RS\n")
        if(water=='b'):
            w=print("Total = 10RS\n")
    elif(menu>4):
        print("Plese Select Valid Option:-")
    w=input(" DO yo wish to continue y/n\n")
    if(w=="n"):
        print("-*-*-*-*-*-*-*-*-*-*Thank You for visiting-*-*-*-*-*-*-*-*-*-*-*")

