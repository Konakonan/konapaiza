import numpy as np

#aは道の数、bは自身の通れる最大降水量の値
a,b=map(int,input().split(" "))

x=[input().split(" ") for i in range(a)]
xx=np.array(x).T #二次元配列を回転？npの行列的な~^^

mydict={index:value for index,value in enumerate(xx,start=1)}

yy=[]
for key,value in mydict.items():
    y=True
    for i in range(a):
        if int(value[i])>=b:
            y=False
            break
        else:
            pass
    if y==True:
        yy.append(key)
    else:
        pass

if len(yy)==0: #リストが空か確かめる、if not yy:でも可能
    print("wait")
else:
    print(*yy) #*yyで配列の要素をアンパックでprintする