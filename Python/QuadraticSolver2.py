#Quadratic Solver pt 2
import math
print("Quadratic Solver: Enter the coefficients for ax^2 = bx + c = 0")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

def doMath(a,b,c):
    d = b**2 - 4*a*c
    return d

def doelseMath(a,b,c):
    return [(-b + math.sqrt(d)) / (2 * a),(-b - math.sqrt(d)) / (2 * a)]

d = doMath(a,b,c)


if d < 0:
   print ("There are no real roots")
elif d == 0:
   print("This equation has one solution: " , doelseMath(a,b,c)[0])
       
else:

    print ("This equation has two solutions: ", doelseMath(a,b,c)[0] ,",", doelseMath(a,b,c)[1])

