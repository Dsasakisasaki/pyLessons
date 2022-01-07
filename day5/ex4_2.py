count=0
print('カレーを召し上がれ')
while True:
    print(f'{count}皿のカレーをたべました')
    ans = input('おかわりはいかがですか？＞＞')
    if ans == 'y':
        count+=1
    else:
        break
    ans = False
print('ごちそうさまでした')
