# coding: utf-8

# 01. 「パタトクカシーー」
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

t = 'パタトクカシーー'
ans = ''.join([ t[i] for i in range(len(t)) if i % 2 != 0 ])
print(ans)

