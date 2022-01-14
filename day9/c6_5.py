class Hero:
    def __init__(self,name='ロト',hp=100):#コンストラクタ　第一引数にselfを入れる
        #引数にデフォルト値を設定しておけば、引数0とかでも呼び出せる
        self.name=name
        self.hp=hp
    name='松田'
    hp=100
    def sleep(self,hours): #self 第一引数に書く　javaはthis
        print('{}は{}時間寝た'.format(self.name,hours))
        self.hp+=hours
#ゲーム開始
print('スッキリファンタジー')
h=Hero('松田',100)
h.sleep(3)
print('{}のHPは現在{}です'.format(h.name,h.hp))


#引数にデフォルト値を設定してあるので、引数0でも使える
h1=Hero()
h1.sleep(100)
print('{}のHPは現在{}です'.format(h1.name,h1.hp))

