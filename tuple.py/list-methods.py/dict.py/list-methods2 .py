
value= [20, 24, 35, 67]
value[0], value[-1] = value[-1], value[0]
print(value)

x = list(input("enter the value :")) 
y = list(input("enter the value :"))
x[0], x[2] = x[2], x[0]
y[0], y[2] = y[2], y[0]
print(x)
print(y)
