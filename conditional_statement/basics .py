a=12345
#rev1 = a % 10
#a//= 10
#rev = (rev1 * 10 )+ a % 10
#a //= 10
rev =0
#print(rev)

l = len(str(a))
for i in range (l):
     lastnum = a % 10
     rev = ( rev * 10 )+ lastnum
     a //= 10
     print("lastnum",lastnum)
     print("a",a)
     
     print("rev",rev)