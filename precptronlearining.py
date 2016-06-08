import random

t = [0,1,0]
x1 = [-2,3,0]
x2 =[1,1,-2]
g = 0
lr = random.uniform(0,1)
def goff(y):
    if y < 0 :
        return 0
    elif y >= 0 :
        return 1

def newwight(w,lr,t,y,x):
    return w + lr * (t-y) *  x
w1 = random.randrange(-30,30)
w2 = random.randrange(-10,70)
i = 0
while g==0:
    iny = x1[i] * w1 + x2[i] * w2
    y = goff(iny)
    if y == t[i]:
        g = 1
        print('phase ',i)
        print(' x1 =',x1[i],'   x2=',x2[i],'  w1=',w1,'   w2=',w2,'  y=',y,'  learining rate is ',lr)
    elif y != t[i] :
        w1 = newwight(w1,lr,t[i],y,x1[i])
        w2 = newwight(w2,lr,t[i],y,x2[i])
    if i >= 2:
        i = 0
    elif i < 2 :
        i +=1


