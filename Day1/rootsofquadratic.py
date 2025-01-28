import math
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
k=b*b-4*a*c
l=2*a
if k>0:
    p= (-b + math.sqrt(k))/l
    q= (-b - math.sqrt(k))/l
    print(f"squareroots are {p:.2f} and {q:.2f}")
elif k==0:
    p=(-b/l)
    print(f"root are: {p:.2f}")
else:
    print("the quadratic equation has no roots")
