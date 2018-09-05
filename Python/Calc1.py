#Python Calculator 1






a = input("Type in number")
b = input("Type another number")

def doMath(a,b,z):
    a = int(a)
    b = int(b)
    if z == 1:
        return(str(a + b))
    if z == 2:
        return(str(a - b))
    if z == 3:
        return(str(a * b))
    if z == 4:
        return(str(round(a / b, 2)))

    if z == 5:
        return(str(a % b))





print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
