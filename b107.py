#カードの枚数をa、1 セットあたりの枚数をb、シャッフルの回数をc
a,b,c=map(int,input().split(" "))
#デッキをセット
x=[i for i in range(1,a+1)]

#セットに分ける関数
#nはリスト、nnは何個ずつに分けるか
def split_list(n,nn):
    for idx in range(0,len(n),nn):
        yield n[idx:idx + nn]

#シャッフルする関数
#qqはsplit_listで作った二次元配列
def syafull(qq):
    total_list=[]
    for i in range(bb):
        q=qq.pop(-1)
        total_list.append(q)
        total_list2=sum(total_list,[])
    return total_list2

while c>=1:
    xx=list(split_list(x,b))
    bb=len(xx)
    x=syafull(xx)
    c-=1

for i in x:
    print(i)
