def eat (**kwargs):
    for key in kwargs:
        print('{}に{}を食べました'.format(key,kwargs[key]))

eat(朝食='納豆',遅めの昼食='パスタ',夕方のおやつ='カレーパン')

def eat2(foods):
    for key in foods:
        print('{}に{}を食べました'.format(key,foods[key]))
#foods={'朝食':'納豆','昼食':'ラーメン'};
#eat2(foods)
eat2({'朝食':'納豆','昼食':'ラーメン'})

