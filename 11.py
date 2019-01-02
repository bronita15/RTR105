#_*_ coding: utf-8 -*-
from math import exp

def mans_exp(x):
    k = 0
    a = ((-1)**k*x**k)/(1)
    S = (1-x) * a
    print("Izdruka no lief.f. a0 = %6.2f S0 = %6.2f"%(a,S))
    
    while k < 1000:
        k = k + 1
        R = ((-1)*x)/k
        a = a * R
        S = S + a
        if k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        elif k == 500:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    return S
print("(1-x)*exp(-x) aprekinasana: ")
x = float(input("Lietotaj, ludzu, ievadi argumentu (x): "))
y = (1-x)*exp(-x)
print("(1-x)*exp(-x) (%.2f) = %6.2f"%(x,y))

yy = mans_exp(x)
print("(1-x)*exp(-x) (%.2f) caur summu: %6.2f"%(x,yy))
