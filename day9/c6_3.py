userinfo = input('名前と血液型をカンマで区切って１行で入力＞＞')
name,blood = userinfo.split(',')
blood = blood.upper().strip()#大文字にしてその後空白取り除く
print('{}さんは{}型なので大吉です'.format(name,blood))
