player1={'国語','算数','理科','社会','英語'}
player2={'国語','算数','音楽','体育','美術'}
input('enterキーを押してください')
common=player1&player2
total=player1|player2
rate=len(common)/len(total)*100
print(f'相性値は{rate}％です')
