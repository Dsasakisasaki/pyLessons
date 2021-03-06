import pprint
data = list()
for i in range(10):
    temp=list()
    for j in range(10):
        temp.append(0)
    data.append(temp)
pprint.pprint(data)

W=10
H=10
data=[None]*H#data=[]だとappendで足すことになるので最初に要素数10の配列を作ったそうすればi(何番目)の指定できる
for i in range(H):
    data[i]=[0]*W
pprint.pprint(data)

data=[[0]*H]*10
pprint.pprint(data)

data[1][1]=5#shallow copy メモリ空間に一つだけなので全ての行に５が入ってしまう
# *　(掛け算)の使用には注意が必要
pprint.pprint(data)

#ほぼこれを使う
data=[[0]*W for i in range(H)]
pprint.pprint(data)



#内包表記
data=[[i*10 + j for j in range(1,11)] for i in range(10)]
pprint.pprint(data)

x=[i for i in range(1,8)]
print(x) #[1,2,3,4,5,6,7]

x=[i**2 for i in range(1,8)]
print(x)

x=[i for i in range(1,8) if i % 2== 0]
print(x)#[2,4,6]

x=[i for i in range(2,7,2)]
print(x)#[2,4,6]

x=[i*10+j for j in range(2,5) for i in range(1,3)]
print(x)#[12,13,14,22,23,24]

x=[[i*10 +j for j in range(7,10)]for i in range(1,3)]

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
print(x) #[[1,0,0][0,1,0][0,0,1]]


