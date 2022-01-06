isError = False
n = 50
if isError == False and n <100:
    print('ok')

if n%2 ==0:
    print('even')
else:
    print('odd')

greeting = input('挨拶をどうぞ＞＞')
if greeting =='こんにちは':
    print('ようこそ')
elif greeting == '景気は？':
    print('ぼちぼちです')
elif greeting == 'さよなら':
    print('お元気で')
else:
    print('どうしました？')
