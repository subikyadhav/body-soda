a = [55, 89, 78, 99, 7]
odd = []
even = []
for i in a:
 if(i % 2 == 0):
    even.append(i)
 elif(i%2 != 0):
    odd.append(i)
print(odd)
print(even)