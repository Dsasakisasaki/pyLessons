members=['工藤','松田','浅木']
print(members)
print(members[0])
print(len(members))
members.append('山田') #追加
print(members)
members[3]='山崎' #要素の書き換え
print(members)
members.remove('山崎')
print(members)
#members.remove(0)#出来ない
del members[0] #index指定での削除はdel文
print(members)

nums=[10,20,30]
print(sum(nums)) #合計60

print(sum(nums)/len(nums)) #平均20

