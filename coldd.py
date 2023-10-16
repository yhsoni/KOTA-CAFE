def cold():
    print("Select Chai By Pressing:-")
    print("Cold Drinks            Can      Bottle")
    print("1 For Coco-Cold:-      50         60\n"
          "2 For Pepsi:-          50         50\n"
          "3 For Limca            45         55\n"
          "4 For Thumbs-up :-     50         60\n"
          "5 For Mirinda:-        45         50\n"
          "6 For Slice:-          40         60\n"
          "7 For Fruity:-         40         60\n")

    x=int(input("Enter Your Choice:-"))
    print("Press\n"
          "C For Can\n"
          "B for bottle\n")
    y=input()
    print("enter the quantity you want:-")
    qu=float(input())
              
    if(x==1 and y=='c'):
        print("Coco-Cold:-      50\n")
        print("tax 7% :-",(qu*50)*0.07)
        print("total:-",(qu*50*0.07)+(qu*50))

    if(x==2 and y=='c'):
        print("Pepsi:-          50\n")
        print("tax 7% :-",(qu*50)*0.07)
        print("total:-",(qu*50*0.07)+(qu*50))
                
    if(x==3 and y=='c'):
        print("Limca            45\n")
        print("tax 7% :-",(qu*45)*0.07)
        print("total:-",(qu*45*0.07)+(qu*45))                  
    if(x==4 and y=='c'):
        print("Thumbs-up :-     50\n")
        print("tax 7% :-",(qu*50)*0.07)
        print("total:-",(qu*50*0.07)+(qu*50))
    if(x==5 and y=='c'):
        print("Mirinda:-        45\n")
        print("tax 7% :-",(qu*45)*0.07)
        print("total:-",(qu*45*0.07)+(qu*45))
    if(x==6 and y=='c'):
        print("Slice:-          40\n")
        print("tax 7% :-",(qu*40)*0.07)
        print("total:-",(qu*40*0.07)+(qu*40))                    
    if(x==7 and y=='c'):
        print("Fruity:-         40\n")
        print("tax 7% :-",(qu*40)*0.07)
        print("total:-",(qu*40*0.07)+(qu*40))
    if(x==1 and y=='b'):
        print("Coco-Cold:-      60\n")
        print("tax 7% :-",(qu*60)*0.07)
        print("total:-",(qu*60*0.07)+(qu*60))
    if(x==2 and y=='b'):
        print("Pepsi:-          55\n")       
        print("tax 7% :-",(qu*55)*0.07)
        print("total:-",(qu*55*0.07)+(qu*55))                
    if(x==3 and y=='b'):
        print("Limca            50\n")
        print("tax 7% :-",(qu*50)*0.07)
        print("total:-",(qu*50*0.07)+(qu*50))                  
    if(x==4 and y=='b'):
        print("Thumbs-up :-     60\n")
        print("tax 7% :-",(qu*60)*0.07)
        print("total:-",(qu*60*0.07)+(qu*60))
    if(x==5 and y=='b'):
        print("Mirinda:-        55\n")
        print("tax 7% :-",(qu*55)*0.07)
        print("total:-",(qu*55*0.07)+(qu*55))                    
    if(x==6 and y=='b'):
        print("Slice:-          60\n")
        print("tax 7% :-",(qu*60)*0.07)
        print("total:-",(qu*60*0.07)+(qu*60))
    if(x==7 and y=='b'):
        print("fruity:-         60\n")
        print("tax 7% :-",(qu*60)*0.07)
        print("total:-",(qu*60*0.07)+(qu*60))
