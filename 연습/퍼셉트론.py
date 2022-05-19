x1=[0,0,1,1]
x2=[0,1,0,1]
d=[0,1,1,1]

n=0.1
b=0.1
w1=0.1
w2=0

for i in range(5):
    for j in range(4):
        if w1*x1[j]+w2*x2[j]+b>=0:
            y=1
        else:
            y=0
        if y!=d[j]:
            w1=w1+n*(d[j]-y)*x1[j]
            w2=w2+n*(d[j]-y)*x2[j]
            b=b+(n*(d[j]-y))
        print("epoch:", i+1, "num:",j+1,"\n", y, d[j]-y, b, w1, w2)
