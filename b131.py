#aは線路数、bは各線路の駅数
a,b=map(int,input().split(" "))
#xは各路線の運賃リスト
x=[input().split(" ") for i in range(a)]
x.insert(0,"None")

#cは乗り換えた回数
c=int(input())
#yは乗り換えた経路
y=[input().split(" ") for i in range(c)]

#totalは合計運賃
total=0
#fは自分が今いる位置
f=0
for i in range(c):
    if f < (int(y[i][1])-1):
        total=total + int(int(x[int(y[i][0])][int(y[i][1])-1]) - int(x[int(y[i][0])][f]))
        f=int(y[i][1])-1

    elif f > (int(y[i][1])-1):
        total =total + int(int(x[int(y[i][0])][f]) - int(x[int(y[i][0])][int(y[i][1])-1]))
        f=int(y[i][1])-1

    elif f == int(int(y[i][1])-1):
        f=int(y[i][1])-1
print(total)
