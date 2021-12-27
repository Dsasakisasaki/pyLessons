scores={'network':60,'database':80,'security':60}
members=['松田','浅木','工藤']
print(tuple(members)) #リストmemberをタプルに変換
print(list(scores)) #scoresのキーをリストに変換
print(set(scores.values())) #scoresの値をセットに変換
#新たにtupleのmembersを一次的に作っているので元のmembersは残っている
color_en=['red','green','blue']
color_ja=['赤','緑','青']
color=dict(zip(color_en,color_ja))
print(color)
