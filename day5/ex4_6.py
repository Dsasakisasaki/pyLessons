numbers=[1,1]
while True:
    n=numbers[-2]+numbers[-1]#ヒボナチス数列　1:1.618
                            #[-1]一番後ろの要素、[-2]後ろから二番目の要素
    if n >= 1000:
        break
    numbers.append(n)
print(numbers)

ratios=[]#レシオ比率
for i in range(1,len(numbers)):#一個先からスタートすれば一個前の取得しやすい
    ratios.append(numbers[i]/numbers[i-1])
print(ratios)

for i in range(len(ratios)):
    ratios[i]= int(ratios[i]*1000)/1000
    #ほかの言語でもこのやり方で少数点以下を処理できる
print(ratios)
