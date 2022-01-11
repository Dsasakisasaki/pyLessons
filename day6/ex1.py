def calc(n,*nums):#n, 必須引数　必ず一個は入れなければエラーになる引数0個対策
    return n+sum(nums)
result=calc(2,3,5)
print(result)

result=calc()
print(result)


