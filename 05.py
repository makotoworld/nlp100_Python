# coding: utf-8

# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

bun = "I am an NLPer"

def n_gram(target, n):
    return [ target[idx:idx + n] for idx in range(len(target) - n + 1)]

# 単語bi-gram
print(n_gram(bun, 2))

# 文字bi-gram
bun = bun.split()
print(n_gram(bun, 2))

