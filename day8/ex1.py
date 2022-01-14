x=[n for n in range(1,8)]
print(x)

x=[i**2 for i in range(1,8)]
print(x)

x=[n for n in range(1,8) if n % 2 ==0]
print(x)

x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)

x=[[i*10+j for j in range(7,10)]for i in range(1,3)]
print(x)

x=[[1 if i==j else 0 for j in range(3)]for i in range(3)]
print(x)



#ジョイタスPython 2次元リスト内包表記演習
import pprint
q1=[[i-j for j in range(10)]for i in range(100,0,-10)]
pprint.pprint(q1)


q2=[[1 if i==j or i+j==4 else 0 for j in range(5)]for i in range(5)]
pprint.pprint(q2)


q3=[[(i*10)-(j*10) for j in range(10)]for i in range(10)]
pprint.pprint(q3)


q4=[[1 if i==j else 2 if j<i else 0 for j in range(5)]for i in range(5)]
pprint.pprint(q4)


q5=[[i+1 if i==j else 0 for j in range(4)]for i in range(4)]
print(q5)


q6=[[i+j for j in range(9)]for i in range(60,100,10)]
print(q6)


q7=[[i*j for j in range(1,10)]for i in range(1,10)]
pprint.pprint(q7)


q8=[[3 if i*j==1 else 7 for j in range(3)]for i in range(3)]
pprint.pprint(q8)
