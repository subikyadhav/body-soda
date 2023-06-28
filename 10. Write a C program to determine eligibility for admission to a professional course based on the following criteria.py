# maths=int(input("enter your maths mark :"))
# physics=int(input("enter your physics mark :"))
# chemistry=int(input("enter your chemistry mark :"))

# if(physics>= 55 and maths>= 65 and chemistry>= 50 and physics + maths + chemistry >=190 ):
#    print("candidate is eligible")
# elif(physics>= 55 and maths>= 65 and chemistry>= 50 and maths + physics >=140):

#      print("candidate is eligible") 
# else:
#      print("candidate is not eligible")     


maths=int(input("enter your maths mark :"))
physics=int(input("enter your physics mark :"))
chemistry=int(input("enter your chemistry mark :"))

total = physics + maths + chemistry
sub2 = maths + physics

if(physics>= 55 and maths>= 65 and chemistry>= 50 and total >=190 or sub2 >=140):
   print("candidate is eligible")

else:
     print("candidate is not eligible")     
