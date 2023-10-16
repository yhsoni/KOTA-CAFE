bill=0
def chai():
    print("Select Chai By Pressing:-")
    print(" ")
    print("1 For Plain Chai:-        5\n"
          "2 For Aadrak Chai:-       10\n"
          "3 For Elichi Chai:-       10\n"
          "4 For Chocolate Chai:-    15\n"
          "5 For Rose Chai:-         15\n"
          "6 For Lemon Chai:-        15\n"
          "7 For Green Chai:-        15\n"
          "8 For Tanoori Chai:-      20\n")
    x=int(input("Enter Your Choice:-"))
    print("select size:-\n"
          "S for Small no extra charge\n"
          "M for Medium extra     + 5/\n"
          "B for Big extra        +10/\n")
    size=input()
    print("A for boan chian             no charge\n"
          "B for Disposal               no charge\n"
          "C for Kulhad                 +2\n")
    cup=input()
    qu=float(input("enter the quantity you want:-"))

#for plain chai
    if(x==1 and size=='s' and cup=='a'):
        print("Plain Chai:-        5\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        bill=qu*5
        print("Total = ",bill)

    if(x==1 and size=='s' and cup=='b'):
        print("Plain Chai:-        5\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*5)
    if(x==1 and size=='s' and cup=='c'):
        print("Plain Chai:-        5\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("No tax")
        print("Total = ",(5+2)*qu)
    if(x==1 and size=='m' and cup=='a'):
        print("Plain Chai:-        5\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*(5+5))
    if(x==1 and size=='m' and cup=='b'):
        print("Plain Chai:-        5\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*(5+5))
    if(x==1 and size=='m' and cup=='c'):
        print("Plain Chai:-        5\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("No tax")
        print("Total = ",qu*(5+5+2))
    if(x==1 and size=='b' and cup=='a'):
        print("Plain Chai:-        5\n"
              "Big size:-        +10\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*(5+10))
    if(x==1 and size=='b' and cup=='b'):
        print("Plain Chai:-        5\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*(5+10))
    if(x==1 and size=='b' and cup=='c'):
        print("Plain Chai:-        5\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("No tax")
        print("Total = ",qu*(5+10+2))

#for adarak chai
    if(x==2 and size=='s' and cup=='a'):
        print("Aadrak Chai:-       10\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*10)

    if(x==2 and size=='s' and cup=='b'):
        print("Aadrak Chai:-       10\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*10)
    if(x==2 and size=='s' and cup=='c'):
        print("Aadrak Chai:-       10\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("No tax")
        print("Total = ",(10+2)*qu)
    if(x==2 and size=='m' and cup=='a'):
        print("Aadrak Chai:-       10\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+5))
    if(x==2 and size=='m' and cup=='b'):
        print("Aadrak Chai:-       10\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+5))
    if(x==2 and size=='m' and cup=='c'):
        print("Aadrak Chai:-       10\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("No tax")
        print("Total = ",qu*(5+10+2))
    if(x==2 and size=='b' and cup=='a'):
        print("Aadrak Chai:-       10\n"
              "Big size:-         +10\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+10))
    if(x==2 and size=='b' and cup=='b'):
        print("Aadrak Chai:-       10\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+10))
    if(x==2 and size=='b' and cup=='c'):
        print("Aadrak Chai:-       10\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("No tax")
        print("Total = ",qu*(10+10+2))


#for elichi chai
    if(x==3 and size=='s' and cup=='a'):
        print("Elichi Chai:-       10\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*10)

    if(x==3 and size=='s' and cup=='b'):
        print("Elichi Chai:-       10\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*10)
    if(x==3 and size=='s' and cup=='c'):
        print("Elichi Chai:-       10\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("No tax")
        print("Total = ",(10+2)*qu)
    if(x==3 and size=='m' and cup=='a'):
        print("Elichi Chai:-       10\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+5))
    if(x==3 and size=='m' and cup=='b'):
        print("Elichi Chai:-       10\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+5))
    if(x==3 and size=='m' and cup=='c'):
        print("Elichi Chai:-       10\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("No tax")
        print("Total = ",qu*(5+10+2))
    if(x==3 and size=='b' and cup=='a'):
        print("Elichi Chai:-       10\n"
              "Big size:-         +10\n"
              "Boan chin:-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+10))
    if(x==3 and size=='b' and cup=='b'):
        print("Elichi Chai:-       10\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("No tax")
        print("Total = ",qu*(10+10))
    if(x==3 and size=='b' and cup=='c'):
        print("Elichi Chai:-       10\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("No tax")
        print("Total = ",qu*(10+10+2))

#for chocolate chai
    if(x==4 and size=='s' and cup=='a'):
        print("Chocolate Chai:-    15\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==4 and size=='s' and cup=='b'):
        print("Chocolate Chai:-    15\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==4 and size=='s' and cup=='c'):
        print("Chocolate Chai:-    15\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("Tax 2.5%:-", qu*17*(0.025))
        print("Total = ",(qu*17*0.025)+(qu*17))
    if(x==4 and size=='m' and cup=='a'):
        print("Chocolate Chai:-    15\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.25)+(qu*20))
    if(x==4 and size=='m' and cup=='b'):
        print("Chocolate Chai:-    15\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==4 and size=='m' and cup=='c'):
        print("Chocolate Chai:-    15\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*22*(0.025))
        print("Total = ",(qu*22*0.025)+(qu*22))
    if(x==4 and size=='b' and cup=='a'):
        print("Chocolate Chai:-    15\n"
              "Big size:-        +10\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.25)+(qu*25))
    if(x==4 and size=='b' and cup=='b'):
        print("Chocolate Chai:-    15\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==4 and size=='b' and cup=='c'):
        print("Chocolate Chai:-    15\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*27*(0.025))
        print("Total = ",(qu*27*0.025)+(qu*27))

#for rose chai
    if(x==5 and size=='s' and cup=='a'):
        print("Rose Chai:-         15\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==5 and size=='s' and cup=='b'):
        print("Rose Chai:-         15\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==5 and size=='s' and cup=='c'):
        print("Rose Chai:-         15\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("Tax 2.5%:-", qu*17*(0.025))
        print("Total = ",(qu*17*0.025)+(qu*17))
    if(x==5 and size=='m' and cup=='a'):
        print("Rose Chai:-         15\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==5 and size=='m' and cup=='b'):
        print("Rose Chai:-         15\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==5 and size=='m' and cup=='c'):
        print("Rose Chai:-         15\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*22*(0.025))
        print("Total = ",(qu*22*0.025)+(qu*22))
    if(x==5 and size=='b' and cup=='a'):
        print("Rose Chai:-         15\n"
              "Big size:-        +10\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==5 and size=='b' and cup=='b'):
        print("Rose Chai:-         15\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==5 and size=='b' and cup=='c'):
        print("Rose Chai:-         15\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*27*(0.025))
        print("Total = ",(qu*27*0.025)+(qu*27))

#for lemon chai
    if(x==6 and size=='s' and cup=='a'):
        print("Lemon Chai:-        15\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==6 and size=='s' and cup=='b'):
        print("Lemon Chai:-        15\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==6 and size=='s' and cup=='c'):
        print("Lemon Chai:-        15\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("Tax 2.5%:-", qu*17*(0.025))
        print("Total = ",(qu*17*0.025)+(qu*17))
    if(x==6 and size=='m' and cup=='a'):
        print("Lemon Chai:-        15\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==6 and size=='m' and cup=='b'):
        print("Lemon Chai:-        15\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==6 and size=='m' and cup=='c'):
        print("Lemon Chai:-        15\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*22*(0.025))
        print("Total = ",(qu*22*0.025)+(qu*22))
    if(x==6 and size=='b' and cup=='a'):
        print("Lemon Chai:-        15\n"
              "Big size:-        +10\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==6 and size=='b' and cup=='b'):
        print("Lemon Chai:-        15\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==6 and size=='b' and cup=='c'):
        print("Lemon Chai:-        15\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*27*(0.025))
        print("Total = ",(qu*27*0.025)+(qu*27))

#for Green tea
    if(x==7 and size=='s' and cup=='a'):
        print("Green Chai:-        15\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==7 and size=='s' and cup=='b'):
        print("Green Chai:-        15\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("Tax 2.5%:-", qu*15*(0.025))
        print("Total = ",(qu*15*0.025)+(qu*15))
    if(x==7 and size=='s' and cup=='c'):
        print("Green Chai:-        15\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("Tax 2.5%:-", qu*17*(0.025))
        print("Total = ",(qu*17*0.025)+(qu*17))
    if(x==7 and size=='m' and cup=='a'):
        print("Green Chai:-        15\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==7 and size=='m' and cup=='b'):
        print("Green Chai:-        15\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==7 and size=='m' and cup=='c'):
        print("Green Chai:-        15\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*22*(0.025))
        print("Total = ",(qu*22*0.025)+(qu*22))
    if(x==7 and size=='b' and cup=='a'):
        print("Green Chai:-        15\n"
              "Big size:-        +10\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==7 and size=='b' and cup=='b'):
        print("Green Chai:-        15\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==7 and size=='b' and cup=='c'):
        print("Green Chai:-        15\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*27*(0.025))
        print("Total = ",(qu*27*0.025)+(qu*27))

#for tandoori chai
    if(x==8 and size=='s' and cup=='a'):
        print("Tanoori Chai:-      20\n"
              "small size:-   no charge\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==8 and size=='s' and cup=='b'):
        print("Tanoori Chai:-      20\n"
              "small size:-   no charge\n"
              "Dispodal :-    no charge\n")
        print("Tax 2.5%:-", qu*20*(0.025))
        print("Total = ",(qu*20*0.025)+(qu*20))
    if(x==8 and size=='s' and cup=='c'):
        print("Tanoori Chai:-      20\n"
              "small size:-   no charge\n"
              "kulhad :-          +2\n")
        print("Tax 2.5%:-", qu*22*(0.025))
        print("Total = ",(qu*22*0.025)+(qu*22))
    if(x==8 and size=='m' and cup=='a'):
        print("Tanoori Chai:-      20\n"
              "Medium size:-      +5\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==8 and size=='m' and cup=='b'):
        print("Tanoori Chai:-      20\n"
              "Medium size:-      +5\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*25*(0.025))
        print("Total = ",(qu*25*0.025)+(qu*25))
    if(x==8 and size=='m' and cup=='c'):
        print("Tanoori Chai:-      20\n"
              "Medium size:-      +5\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*27*(0.025))
        print("Total = ",(qu*27*0.025)+(qu*27))
    if(x==8 and size=='b' and cup=='a'):
        print("Tanoori Chai:-      20\n"
              "Big size:-        +10\n"
              "Boan chin:-    no charge\n")
        print("Tax 2.5%:-", qu*30*(0.025))
        print("Total = ",(qu*30*0.025)+(qu*30))
    if(x==8 and size=='b' and cup=='b'):
        print("Tanoori Chai:-      20\n"
              "Big size:-         +10\n"
              "Disposal :-    no charge\n")
        print("Tax 2.5%:-", qu*30*(0.025))
        print("Total = ",(qu*30*0.025)+(qu*30))
    if(x==8 and size=='b' and cup=='c'):
        print("Tanoori Chai:-      20\n"
              "Big size:-        +10\n"
              "Kulhad:-           +2\n")
        print("Tax 2.5%:-", qu*32*(0.025))
        print("Total = ",(qu*32*0.025)+(qu*32))
