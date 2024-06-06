#aは歌う人数、bは課題曲のコード数
a,b=map(int,input().split(" "))
#xは課題曲の正解コード
x=[input() for i in range(b)]
#xxは歌った人の各Hzを表す二次元配列
xx=[[input() for i in range(b)] for i in range(a)]

totalscorelist=[]
score=100
for i in range(a):
    for j in range(b):
        if int(x[j])-int(xx[i][j])==0:
            score+=0
        elif abs(int(x[j])-int(xx[i][j]))<=10:
            score -=1
        elif 10<abs(int(x[j])-int(xx[i][j]))<=20:
            score -=2
        elif 20<abs(int(x[j])-int(xx[i][j]))<=30:
            score -=3
        else:
            score-=5
    totalscorelist.append(score)
    score=100

maxscore=0
for i in range(a):
    if int(totalscorelist[i])>=maxscore:
        maxscore=int(totalscorelist[i])
if maxscore==0:
    print(0)
else:
    print(maxscore)
