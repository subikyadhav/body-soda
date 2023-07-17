value=int(input( " enter the month : "))
if(value == 1):
   print(" 31 day")
elif(value == 3 or value == 5 or value == 7 or value == 9 or value == 11):
     print(" 31 days ")
elif(value == 4 or value == 6 or value == 8 or value == 10 or value == 12 ):
     print(" 30 days ")
else:
    print(" 28  or 29 days ")     
            
