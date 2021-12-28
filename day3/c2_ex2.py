scores={}
scores['国語']=int(input('国語の点数を入力>'))
scores['算数']=int(input('算数の点数を入力>'))
scores['理科']=int(input('理科の点数を入力>'))
scores['社会']=int(input('社会の点数を入力>'))
scores['英語']=int(input('英語の点数を入力>'))
total=sum(scores.values())
print(total)
print(total/len(scores))
#let li=[];
#li.push(10);
#li.push(20);
#for(let i=0;i<li.lenght;i++){
#sum+=li[i];
#}
#console.log(`合計点${sum},平均点${sum/li.length}`)
print(f'合計点{total},平均点{total/len(scores)}')
