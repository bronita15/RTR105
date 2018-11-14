from decimal import Decimal
import math

X = Decimal('10')


def my_exp(x):
    k = 0
    a = Decimal('0')
    for k in range(1000):
        a += (Decimal('-1.00')**k)*(x**k)/ math.factorial(k)
        S = S + a
    return (Decimal('1')-x*a)
    print(a,k,S)

x = float(input("Lietotāj, lūdzu ievadi argumentu (x): "))
print((Decimal('1') - X) * Decimal(math.exp(-X)))
print(my_exp(X))

