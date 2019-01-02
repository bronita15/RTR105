import math

def mans_exp(x):
    k = 0
    a = ((-1)**k*x**k)/k
    x = float(input("Lietotaj, ludzu, ievadi argumentu (x): "))
    
    while k < 1000:
        k = k + 1
        R = ((-1)**k*x**k)/k
        a = a * R
        S = (1-x) * a
    print(S,a)
