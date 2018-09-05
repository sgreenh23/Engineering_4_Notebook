#Quadratic Solver
import math
print("Quadratic Solver: Enter the coefficients for ax^2 = bx + c = 0")
a = input("a=")
b = input("b=")
c = input("c=")

#def doMath(a,b,c):
a = int(a)
b = int(b)
c = int(c)
d = b**2-4*a*c

if d < 0:
   print ("There are no real roots")
elif d == 0:
   x = -b+math.sqrt(d) / (2 * a)
   print("This equation has one solution: " ,x)
       
else:
    x1 = -b + math.sqrt(d) / (2 * a) 
    x2 = -b + math.sqrt(d) / (2 * a) 
    print ("This equation has two solutions: ", x1, "and", x2)
