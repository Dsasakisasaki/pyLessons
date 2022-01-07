def eat(breakfast,luch='ラーメン',dinner='カレー'):
    print('朝は{}を食べました'.format(breakfast))
    print('昼は{}を食べました'.format(luch))
    print('夜は{}を食べました'.format(dinner))
eat(breakfast='納豆ご飯',dinner='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ごはん')
eat('納豆ごはん',dinner='カレーうどん')
