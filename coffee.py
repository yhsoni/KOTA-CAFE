def coffee():
    print("Select Chai By Pressing:-")
    print(" ")
    print("1 For Plain Hot Coffee:-                 20\n"
          "2 For Strong Coffee:-                    25\n"
          "3 Black Coffe:-                          30\n"
          "4 For Hot Chocolate Coffee:-             30\n"
          "5 For Cappaccino:-                       50\n"
          "6 For Cold Coffee:-                      50\n"
          "7 For Cold Coffee With Ice-cream:-       70\n")
    x=int(input("Enter Your Choice:-"))
    print("select size:-\n"
          "S for Small no extra charge\n"
          "M for Medium extra     + 5/\n"
          "B for Big extra        +10/\n")
    size=input()
    print("A for Paper glass                         +1\n"
          "B for Disposal glass               no charge\n"
          "C for Kulhad                              +2\n")
    cup=input()
    qu=float(input("enter the quantity you want:-"))

#plain coffee
    if(x==1 and size=='s' and cup=='a'):
        print("Plain Hot Coffee:-    20\n"
              "small size:-   no charge\n"
              "Paper glass:-       +1\n")
        print("Tax  5% =", 0.05*21*qu)
        print("Total = ",(0.05*21*qu)+(qu*21))
    if(x==1 and size=='s' and cup=='b'):
        print("Plain Hot Coffee:-    20\n"
              "small size:-         no charge\n"
              "Dispodal glass :-    no charge\n")
        print("Tax  5% =", 0.05*20*qu)
        print("Total = ",(0.05*20*qu)+(qu*20))
    if(x==1 and size=='s' and cup=='c'):
        print("Plain Hot Coffee:-    20\n"
              "small size:-         no charge\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*22*qu)
        print("Total = ",(0.05*22*qu)+(qu*22))

    if(x==1 and size=='m' and cup=='a'):
        print("Plain Hot Coffee:-    20\n"
              "Medium size:-        + 5\n"
              "Paper glass:-        +1\n")
        print("Tax  5% =", 0.05*26*qu)
        print("Total = ",(0.05*26*qu)+(qu*26))
    if(x==1 and size=='m' and cup=='b'):
        print("Plain Hot Coffee:-    20\n"
              "Medium size:-         + 5\n"
              "Dispodal glass :-     no charge\n")
        print("Tax  5% =", 0.05*25*qu)
        print("Total = ",(0.05*25*qu)+(qu*25))
    if(x==1 and size=='m' and cup=='c'):
        print("Plain Hot Coffee:-    20\n"
              "Medium size:-       + 5\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*27*qu)
        print("Total = ",(0.05*27*qu)+(qu*27))

    if(x==1 and size=='b' and cup=='a'):
        print("Plain Hot Coffee:-   20\n"
              "Big size:-          + 10\n"
              "Paper glass:-       +1\n")
        print("Tax  5% =", 0.05*31*qu)
        print("Total = ",(0.05*31*qu)+(qu*31))
    if(x==1 and size=='b' and cup=='b'):
        print("Plain Hot Coffee:-   20\n"
              "Big size:-           10\n"
              "Dispodal glass :-    no charge\n")
        print("Tax  5% =", 0.05*30*qu)
        print("Total = ",(0.05*30*qu)+(qu*30))
    if(x==1 and size=='b' and cup=='c'):
        print("Plain Hot Coffee:-    20\n"
              "Big size:-           +10\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*32*qu)
        print("Total = ",(0.05*32*qu)+(qu*32))


#for strong coffee
    if(x==2 and size=='s' and cup=='a'):
        print("Strong Coffee:-      25\n"
              "small size:-         no charge\n"
              "Paper glass:-        1\n")
        print("Tax  5% =", 0.05*26*qu)
        print("Total = ",(0.05*26*qu)+(qu*26))
    if(x==2 and size=='s' and cup=='b'):
        print("Strong Coffee:-         25\n"
              "small size:-         no charge\n"
              "Dispodal glass :-    no charge\n")
        print("Tax  5% =", 0.05*25*qu)
        print("Total = ",(0.05*25*qu)+(qu*25))
    if(x==2 and size=='s' and cup=='c'):
        print("Strong Coffee:-       25\n"
              "small size:-          no charge\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*27*qu)
        print("Total = ",(0.05*27*qu)+(qu*27))

    if(x==2 and size=='m' and cup=='a'):
       print("Strong Coffee:-        25\n"
              "Medium size:-        + 5\n"
              "Paper glass:-        +1\n")
       print("Tax  5% =", 0.05*30*qu)
       print("Total = ",(0.05*30*qu)+(qu*30))
    if(x==2 and size=='m' and cup=='b'):
        print("Strong Coffee:-       25\n"
              "Medium size:-         + 5\n"
              "Dispodal glass :-     no charge\n")
        print("Tax  5% =", 0.05*30*qu)
        print("Total = ",(0.05*30*qu)+(qu*30))
    if(x==2 and size=='m' and cup=='c'):
        print("Strong Coffee:-      25\n"
              "Medium size:-        5\n"
              "Kulhad glass :-      2\n")
        print("Tax  5% =", 0.05*32*qu)
        print("Total = ",(0.05*32*qu)+(qu*32))

    if(x==2 and size=='b' and cup=='a'):
       print("Strong Coffee:-      25\n"
              "Big size:-          + 10\n"
              "Paper glass:-       +1\n")
       print("Tax  5% =", 0.05*36*qu)
       print("Total = ",(0.05*36*qu)+(qu*36))
    if(x==2 and size=='b' and cup=='b'):
        print("Strong Coffee:-     25\n"
              "Big size:-          + 10\n"
              "Dispodal glass :-   no charge\n")
        print("Tax  5% =", 0.05*30*qu)
        print("Total = ",(0.05*30*qu)+(qu*30))
    if(x==2 and size=='b' and cup=='c'):
        print("Strong Coffee:-      25\n"
              "Big size:-           +10\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*37*qu)
        print("Total = ",(0.05*37*qu)+(qu*37))


#for black coffee
    if(x==3 and size=='s' and cup=='a'):
        print("Black Coffe:-       30\n"
              "small size:-        no charge\n"
              "Paper glass:-       +1\n")
        print("Tax  5% =", 0.05*31*qu)
        print("Total = ",(0.05*31*qu)+(qu*31))
    if(x==3 and size=='s' and cup=='b'):
        print("Black Coffe:-        30\n"
              "small size:-         no charge\n"
              "Dispodal glass :-    no charge\n")
        print("Tax  5% =", 0.05*30*qu)
        print("Total = ",(0.05*30*qu)+(qu*30))
    if(x==3 and size=='s' and cup=='c'):
        print("Black Coffe:-        30\n"
              "small size:-         no charge\n"
              "Kulhad glass :-      2\n")
        print("Tax  5% =", 0.05*32*qu)
        print("Total = ",(0.05*32*qu)+(qu*32))

    if(x==3 and size=='m' and cup=='a'):
       print("Black Coffe:-         30\n"
              "Medium size:-        + 5\n"
              "Paper glass:-        +1\n")
       print("Tax  5% =", 0.05*36*qu)
       print("Total = ",(0.05*36*qu)+(qu*36))
    if(x==3 and size=='m' and cup=='b'):
        print("Black Coffe:-       30\n"
              "Medium size:-       + 5\n"
              "Dispodal glass :-   no charge\n")
        print("Tax  5% =", 0.05*36*qu)
        print("Total = ",(0.05*36*qu)+(qu*36))
    if(x==3 and size=='m' and cup=='c'):
        print("Black Coffe:-       30\n"
              "Medium size:-       + 5\n"
              "Kulhad glass :-      2\n")
        print("Tax  5% =", 0.05*37*qu)
        print("Total = ",(0.05*37*qu)+(qu*37))

    if(x==3 and size=='b' and cup=='a'):
       print("Black Coffe:-        30\n"
              "Big size:-          + 10\n"
              "Paper glass:-       +1\n")
       print("Tax  5% =", 0.05*41*qu)
       print("Total = ",(0.05*41*qu)+(qu*41))
    if(x==3 and size=='b' and cup=='b'):
        print("Black Coffe:-       30"
              "Big size:-          + 10\n"
              "Dispodal glass :-   no charge\n")
        print("Tax  5% =", 0.05*40*qu)
        print("Total = ",(0.05*40*qu)+(qu*40))
    if(x==3 and size=='b' and cup=='c'):
        print("Black Coffe:-        30\n"
              "Big size:-           +10\n"
              "Kulhad glass :-      2\n")
        print("Tax  5% =", 0.05*42*qu)
        print("Total = ",(0.05*42*qu)+(qu*42))


#for chocolate coffee
    if(x==4 and size=='s' and cup=='a'):
        print("Hot Chocolate Coffee:-             30\n"
              "small size:-                 no charge\n"
              "Paper glass:-               +1\n")
        print("Tax  5% =", 0.05*31*qu)
        print("Total = ",(0.05*31*qu)+(qu*31))
    if(x==4 and size=='s' and cup=='b'):
        print("Hot Chocolate Coffee:-             30\n"
              "small size:-                    no charge\n"
              "Dispodal glass :-               no charge\n")
        print("Tax  5% =", 0.05*30*qu)
        print("Total = ",(0.05*30*qu)+(qu*30))
    if(x==4 and size=='s' and cup=='c'):
        print("Hot Chocolate Coffee:-      30\n"
              "small size:-                no charge\n"
              "Kulhad glass :-             2\n")
        print("Tax  5% =", 0.05*32*qu)
        print("Total = ",(0.05*32*qu)+(qu*32))

    if(x==4 and size=='m' and cup=='a'):
       print("Hot Chocolate Coffee:-    30\n"
              "Medium size:-            + 5\n"
              "Paper glass:-            +1\n")
       print("Tax  5% =", 0.05*36*qu)
       print("Total = ",(0.05*36*qu)+(qu*36))
    if(x==4 and size=='m' and cup=='b'):
        print("Hot Chocolate Coffee:-     30\n"
              "Medium size:-              + 5\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*35*qu)
        print("Total = ",(0.05*35*qu)+(qu*35))
    if(x==4 and size=='m' and cup=='c'):
        print("Hot Chocolate Coffee:-   30\n"
              "Medium size:-            + 5\n"
              "Kulhad glass :-          2\n")
        print("Tax  5% =", 0.05*37*qu)
        print("Total = ",(0.05*37*qu)+(qu*37))

    if(x==4 and size=='b' and cup=='a'):
       print("Hot Chocolate Coffee:-          30\n"
              "Big size:-                     + 10\n"
              "Paper glass:-                  +1\n")
       print("Tax  5% =", 0.05*41*qu)
       print("Total = ",(0.05*41*qu)+(qu*41))
    if(x==4 and size=='b' and cup=='b'):
        print("Hot Chocolate Coffee:-    30\n"
              "Big size:-                + 10\n"
              "Dispodal glass :-         no charge\n")
        print("Tax  5% =", 0.05*40*qu)
        print("Total = ",(0.05*40*qu)+(qu*40))
    if(x==4 and size=='b' and cup=='c'):
        print("Hot Chocolate Coffee:-        30\n"
              "Big size:-                   +10\n"
              "Kulhad glass :-               2\n")
        print("Tax  5% =", 0.05*42*qu)
        print("Total = ",(0.05*42*qu)+(qu*42))


####for cappaccino
    if(x==5 and size=='s' and cup=='a'):
        print("Cappaccino:-                 50\n"
              "small size:-                 no charge\n"
              "Paper glass:-               +1\n")
        print("Tax  5% =", 0.05*51*qu)
        print("Total = ",(0.05*51*qu)+(qu*51))
    if(x==5 and size=='s' and cup=='b'):
        print("Cappaccino:-                       50\n"
              "small size:-                    no charge\n"
              "Dispodal glass :-               no charge\n")
        print("Tax  5% =", 0.05*50*qu)
        print("Total = ",(0.05*50*qu)+(qu*50))
    if(x==5 and size=='s' and cup=='c'):
        print("Cappaccino:-                 50\n"
              "small size:-                 no charge\n"
              "Kulhad glass :-              2\n")
        print("Tax  5% =", 0.05*52*qu)
        print("Total = ",(0.05*52*qu)+(qu*52))

    if(x==5 and size=='m' and cup=='a'):
       print("Cappaccino:-              50\n"
              "Medium size:-            + 5\n"
              "Paper glass:-            +1\n")
       print("Tax  5% =", 0.05*56*qu)
       print("Total = ",(0.05*56*qu)+(qu*56))
    if(x==5 and size=='m' and cup=='b'):
        print("Cappaccino:-               50\n"
              "Medium size:-              + 5\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*55*qu)
        print("Total = ",(0.05*55*qu)+(qu*55))
    if(x==5 and size=='m' and cup=='c'):
        print("Cappaccino:-               50\n"
              "Medium size:-            + 5\n"
              "Kulhad glass :-          2\n")
        print("Tax  5% =", 0.05*57*qu)
        print("Total = ",(0.05*57*qu)+(qu*57))

    if(x==5 and size=='b' and cup=='a'):
       print("Cappaccino:-                    50\n"
              "Big size:-                     + 10\n"
              "Paper glass:-                  +1\n")
       print("Tax  5% =", 0.05*61*qu)
       print("Total = ",(0.05*61*qu)+(qu*61))
    if(x==5 and size=='b' and cup=='b'):
        print("Cappaccino:-               50\n"
              "Big size:-                 + 10\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*60*qu)
        print("Total = ",(0.05*60*qu)+(qu*60))
    if(x==5 and size=='b' and cup=='c'):
        print("Cappaccino:-          50\n"
              "Big size:-           +10\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*62*qu)
        print("Total = ",(0.05*62*qu)+(qu*62))


###cold coffee
    if(x==6 and size=='s' and cup=='a'):
        print("Cold Coffee:-                 50\n"
              "small size:-                 no charge\n"
              "Paper glass:-               +1\n")
        print("Tax  5% =", 0.05*51*qu)
        print("Total = ",(0.05*51*qu)+(qu*51))
    if(x==6 and size=='s' and cup=='b'):
        print("Cold Coffee:-                       50\n"
              "small size:-                    no charge\n"
              "Dispodal glass :-               no charge\n")
        print("Tax  5% =", 0.05*50*qu)
        print("Total = ",(0.05*50*qu)+(qu*50))
    if(x==6 and size=='s' and cup=='c'):
        print("Cold Coffee:-                 50\n"
              "small size:-                 no charge\n"
              "Kulhad glass :-              2\n")
        print("Tax  5% =", 0.05*52*qu)
        print("Total = ",(0.05*52*qu)+(qu*52))

    if(x==6 and size=='m' and cup=='a'):
       print("Cold Coffee:-              50\n"
              "Medium size:-            + 5\n"
              "Paper glass:-            +1\n")
       print("Tax  5% =", 0.05*56*qu)
       print("Total = ",(0.05*56*qu)+(qu*56))
    if(x==6 and size=='m' and cup=='b'):
        print("Cold Coffee:-               50\n"
              "Medium size:-              + 5\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*55*qu)
        print("Total = ",(0.05*55*qu)+(qu*55))
    if(x==6 and size=='m' and cup=='c'):
        print("Cold Coffee:-            50\n"
              "Medium size:-            + 5\n"
              "Kulhad glass :-          2\n")
        print("Tax  5% =", 0.05*57*qu)
        print("Total = ",(0.05*57*qu)+(qu*57))

    if(x==6 and size=='b' and cup=='a'):
       print("Cold Coffee:-                    50\n"
              "Big size:-                     + 10\n"
              "Paper glass:-                  +1\n")
       print("Tax  5% =", 0.05*61*qu)
       print("Total = ",(0.05*61*qu)+(qu*61))
    if(x==6 and size=='b' and cup=='b'):
        print("Cold Coffee:-               50\n"
              "Big size:-                 + 10\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*60*qu)
        print("Total = ",(0.05*60*qu)+(qu*60))
    if(x==6 and size=='b' and cup=='c'):
        print("Cold Coffee:-        50\n"
              "Big size:-           +10\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*62*qu)
        print("Total = ",(0.05*62*qu)+(qu*62))


###coffee with ice cream
    if(x==7 and size=='s' and cup=='a'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "small size:-                 no charge\n"
              "Paper glass:-               +1\n")
        print("Tax  5% =", 0.05*71*qu)
        print("Total = ",(0.05*71*qu)+(qu*71))
    if(x==7 and size=='s' and cup=='b'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "small size:-                    no charge\n"
              "Dispodal glass :-               no charge\n")
        print("Tax  5% =", 0.05*70*qu)
        print("Total = ",(0.05*70*qu)+(qu*70))
    if(x==7 and size=='s' and cup=='c'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "small size:-                 no charge\n"
              "Kulhad glass :-              2\n")
        print("Tax  5% =", 0.05*72*qu)
        print("Total = ",(0.05*72*qu)+(qu*72))

    if(x==7 and size=='m' and cup=='a'):
       print("Cold Coffee With Ice-cream:-       70\n"
              "Medium size:-            + 5\n"
              "Paper glass:-            +1\n")
       print("Tax  5% =", 0.05*76*qu)
       print("Total = ",(0.05*76*qu)+(qu*76))
    if(x==7 and size=='m' and cup=='b'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "Medium size:-              + 5\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*75*qu)
        print("Total = ",(0.05*75*qu)+(qu*75))
    if(x==7 and size=='m' and cup=='c'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "Medium size:-            + 5\n"
              "Kulhad glass :-          2\n")
        print("Tax  5% =", 0.05*77*qu)
        print("Total = ",(0.05*77*qu)+(qu*77))

    if(x==7 and size=='b' and cup=='a'):
       print("Cold Coffee With Ice-cream:-       70\n"
              "Big size:-                     + 10\n"
              "Paper glass:-                  +1\n")
       print("Tax  5% =", 0.05*81*qu)
       print("Total = ",(0.05*81*qu)+(qu*81))
    if(x==7 and size=='b' and cup=='b'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "Big size:-                 + 10\n"
              "Dispodal glass :-          no charge\n")
        print("Tax  5% =", 0.05*80*qu)
        print("Total = ",(0.05*80*qu)+(qu*80))
    if(x==7 and size=='b' and cup=='c'):
        print("Cold Coffee With Ice-cream:-       70\n"
              "Big size:-           +10\n"
              "Kulhad glass :-       2\n")
        print("Tax  5% =", 0.05*82*qu)
        print("Total = ",(0.05*82*qu)+(qu*82))
