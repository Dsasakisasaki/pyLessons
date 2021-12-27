a=[10,20,30,40,50]
#基本
print(a[1:3]) #index1から3の前まで3含まない
b=a[1:3] #新しい配列を作っているのでこう書くのと同じ
print(b)
print(a[2:])

print(a[:3])

#負のインデックスについて
print(a[-1]) #indexには負の値が使え後ろからを意味する50
print(a[-2]) #40
print(a[-3:]) #30,40,50 後ろから三番目からスタートして残り全部

#スライス時には範囲外でもエラーにならない　ある分だけ
print(a[0:100]) #[10,20,30,40,50]
#print(a[100]) エラー

#リストのコピー作成
x=[100,200,300]
y=x[:]
x[0]=500
print(y[0]) #100

b=a[:] #aのコピーができる　参照値の代入ではない

#以下の方法だとｙとｘは同じリストを指す
x=[100,200,300]
y=x
x[0]=500
print(y[0])

#スライス時の第三引数(step)
a=[1,2,3,4,5,6,7,8,9]
print(a[1:7:2]) #[2,4,6] スタートindex1、ラスト7の範囲で２つ飛ばしながら
print(a[5:2:-1]) #[6,5,4]
print(a[::-1]) #配列のリバース　端から端までを反転　#[9,8,,,,,1]

#文字列でも同様
s='Hello world'
s2=s[1:5]
print(s2)
print(s[::-1]) #dllrow olleH
print(s[-1]) #d


