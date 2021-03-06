import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

# N vienmerigi sadaliti gadijuma skaitli
# N uniformly destributed random numbers

from numpy import random
#print(random.__doc__)
#print(random.uniform.__doc__)

N = 10000
a = 0
b = 5

#pseido-gadijuma skaitli generatora grauds
random.seed(1)

x = random.uniform(a,b,N)

'''
k = [0, 0, 0, 0, 0]
for i in range(N):
    if x[i] < 1:
        k[0] = k[0] + 1
    elif x[i] < 2:
        k[1] = k[1] + 1
    elif x[i] < 3:
        k[2] = k[2] + 1
    elif x[i] < 4:
        k[3] = k[3] + 1
    else:
        k[4] = k[4] + 1
print(k)
'''


y = random.uniform(a,b,N)

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('funkcijas un tas integralis (laukums starp funkciju un x ass)')
#nav jegas zimet sadi plt.plot(x,y)
#plt.plot(x,y,'ko')
N1 = 0
for i in range(N):
    if y[i] < x[i]:
        plt.plot(x[i],y[i],'go')
        N1 = N1 +1
    else:
        plt.plot(x[i],y[i],'ro')


S_zinamais = (b-a) * (b-a)
S_nezinamais = 1. * S_zinamais * N1 / N
print(S_nezinamais)

plt.show()
