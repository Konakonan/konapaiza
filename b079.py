#xはaを1~zを26に対応した辞書リスト
x={chr(i):i-96 for i in range(ord("a"),ord("z")+1)}

#xxは入力文字を格納するリスト
xx=input().split(" ")
xx2=list(reversed(xx))


p=[]
k=[]
for i in xx:
    for j in i:
        p.append(x[j])


for i in xx2:
    for j in i:
        k.append(x[j])


#リストの要素を足し算して新しいリストを生成する関数
def aa(a:list):
    q=[]
    for i in range(len(a)-1):
        total=a[i]+a[i+1]
        if total>=101:
            total=total-101
        q.append(total)
    return q


while len(p)>1:
    p=aa(p)
    k=aa(k)

if p[0]>k[0]:
    print(*p)
else:
    print(*k)