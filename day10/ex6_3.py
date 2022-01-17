def welcome(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age'] = u['age'] +1
    print('あなたは来年{}歳だから大吉です'.format(u['age']))

username = input('名前を入力＞＞')
userage = int(input('年齢を入力＞＞'))
user = {'name':username,'age':userage}
copied_user = user.copy()
welcome(copied_user)
print('{}歳の{}さん、またプレイしてくださいね'.format(user['age'],user['name']))

