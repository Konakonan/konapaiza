a=int(input())
x=[input() for i in range(a)]
n=0
for i in range(a):
    if n<=int(x[i]):
        n=int(x[i])
xx=len(x)

count=0
z=1
while int(xx)>0:
    if int(x[0])==z:
        del x[0]
        z +=1
        xx=len(x)

    elif int(x[0])!=z and int(x[0])!=int(n):
        b=x.pop(0)
        x.append(b)

    elif int(x[0])!=z and int(x[0])==int(n):
        b=x.pop(0)
        x.append(b)
        count+=1


print(count)
