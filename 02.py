# coding: utf-8

# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

t1 = 'パトカー'
t2 = 'タクシー'
ans = ''.join([t1[i] + t2[i] for i in range(len(t1))])
print(ans)