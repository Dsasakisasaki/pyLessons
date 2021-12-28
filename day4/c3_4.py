name=input('名前＞＞')
print('{}さんこんにちは'.format(name))
food=input('{}さんの好きな食べ物＞＞'.format(name))
if 'カレー' in food:
    print('素敵')
else:
    print('わたしも{}がすきです'.format(food))

n=10
if n in [5,10,15]:
    print('ok')
else:
    print('ng')

key='red'
if key in {'red':'赤','blue':'青'}:
    print('ok')
else:
    print('ng')
