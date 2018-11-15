import math

def my_exp(x):
    k = 0
    a = (1-x)*((-1)**k*x**k/(1))
    S = a
    while k < 1000:
        k = k + 1
        a = a * (1-x)*((-1)**k*x**k/ (math.factorial(k)))
        S = S + a
        print(k,S)

x = float(input("Lietotāj, lūdzu ievadi argumentu (x): "))
y = my_exp(x)
print(x,y)
