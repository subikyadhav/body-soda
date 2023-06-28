rollno=int(input("enter the roll number :"))
Student_name =input("enter your name :")
Marks_for_Physics= int(input("enter the phy. mark :"))
Marks_for_Chemistry= int(input("enter the chem. mark :")) 
Marks_for_Computer_Application= int(input("enter the c.a mark :")) 
total= int(Marks_for_Physics+Marks_for_Chemistry+Marks_for_Computer_Application)
percantage= int(total/3) 

print(rollno)
print(Student_name)
print(Marks_for_Physics)
print(Marks_for_Chemistry)
print(Marks_for_Computer_Application)
print("total :",total)
print("percantage :", percantage)
if(total>=300):
    print("first division")
elif(total>=250):
     print("second division")
else:
     print("third division")     