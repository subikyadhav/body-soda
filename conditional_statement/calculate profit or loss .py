cost1=int(input("enter the cost value :"))
cost2=int(input("enter the selling price :"))

if(cost1 < cost2 ):
    
    profit= cost2 / cost1
    print( "profit:",profit)
elif(cost1 > cost2 ):
    loss= cost2 - cost1 
    print( "loss:",loss)    
else:
    print(" no profit , no loss")    
