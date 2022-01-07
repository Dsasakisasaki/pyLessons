"""temp =list()
for n in range(10):
    data=float(input(f'{n+1}個目のデータを入力＞＞'))
    temp.append(data)
for count in range(len(temp)):
    print(f'{count+8}時{temp[count]}度')

temp_new =list()
for count in range (len(temp)):
    if count == 5:
        temp_new.append('N/A')
    else:
        temp_new.append(temp[count])
print(temp)
print(temp_new)

total = 0
for date in temp_new:
    if isinstance(data,float):
        total=total+data
print(total/(len(temp_new)-1))
"""

temp=[7.8,9.1,10.2,11.0,12.5,12.4,14.3,13.8,12.9,12.4]
for t in temp:
    print(t,end=',')
print()
temp_new=temp[:] #[:]配列のコピー
temp_new[5]='N/A'
samples=[]
for t in temp_new:
    print(t,end=',')
    if not isinstance(t,float):#フロートだけ抜き出す
        continue
    samples.append(t)
print()
print(f'平均気温:{sum(samples)/len(samples)}')
