def snacks():
    print("Select Chai By Pressing:-")
    print(" ")
    print("1 For Plain Biscuts:-       10\n"
          "2 For Cookies:-             20\n"
          "3 For Chocolate Cookies:-   40\n"
          "4 For Chocolate Biscuts:-   20\n"
          "5 For Matari                5\n"
          "6 For Masala Matari         7\n")

    x=int(input("Enter Your Choice:-"))
    print("enter the quantity you want:-")
    qu=float(input())
    if(x==1):
        print("Plain Biscuts:-       10\n")
        print("tax 5% :-",(qu*10)*0.05)
        print("total:-",(qu*10*0.05)+(qu*10)) 

    if(x==2):
        print("Cookies:-             20\n")       
        print("tax  5% :-",(qu*20)*0.05)
        print("total:-",(qu*20*0.05)+(qu*20)) 

    
    if(x==3):
        print("Chocolate Cookies:-   40\n")
        print("tax 5% :-",(qu*40)*0.05)
        print("total:-",(qu*40*0.05)+(qu*40)) 

      
    if(x==4):
        print("Chocolate Biscuts:-   20\n")
        print("tax 5% :-",(qu*20)*0.05)
        print("total:-",(qu*20*0.05)+(qu*20)) 


    if(x==5):
        print("Matari                5\n")
        print("tax :5% -",(qu*5)*0.05)
        print("total:-",(qu*5*0.05)+(qu*5)) 


    if(x==6):
        print("Masala Matari         7\n")
        print("tax 5% :-",(qu*7)*0.05)
        print("total:-",(qu*7*0.05)+(qu*7)) 

