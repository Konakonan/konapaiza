#aは箱の数、bは球の半径
a,b=map(int,input().split(" "))
#bbは球の直径
bb=b*2
x=[input().split(" ") for i in range(a)]

#enumerate関数でindexをつけて(start=1を指定)、辞書型を生成
mydict={index:value for index,value in enumerate(x,start=1)}

y=True
for key,value in mydict.items():#item()でkeyとvalue(ここではlist型)を取り出す
    y=True
    for i in range(3):
        if int(value[i])<bb:#listの要素をひとつずつ取り出す
            y=False
            break #ひとつでも箱の一辺が球の直径より小さかたらfor文を抜ける
    if y==True:
        print(key)