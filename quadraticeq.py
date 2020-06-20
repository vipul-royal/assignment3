import math
a=float(input("Enter the Value Of a="))
b=float(input("Enter the Value Of b="))
c=float(input("Enter the Value Of c="))
if(a!=0):
    d=b**2-4*a*c
    if d==0:
        x1,x2=-b/(2*a),-b/(2*a)
        print("The Roots Are Real x1=",x1," x2=",x2)
    elif d>0:
        x1,x2=(-b+math.sqrt(d))/(2*a),(-b -math.sqrt(d))/(2*a)
        print("The Roots Are Different x1=",x1," x2=",x2)
    else:
        print("The Roots Are Imaginary")
else:
    print("It is a Linear Equation")