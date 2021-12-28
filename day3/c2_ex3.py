hb1={'国語','算数','理科','社会','英語'}
hb2={'国語','算数','音楽','体育','美術'}
input('enterキーを押してください')
common=hb1&hb2
total=hb1|hb2
rate=len(common)/len(total)*100
print(f'相性値は{rate}％です')
#print(f'二人の相性値{len(hb1 & hb2) /len(hb1 | hb2) * 100}%です')
