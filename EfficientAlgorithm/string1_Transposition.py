def anargams(w):
    w = list(set(w)) # 去除重复的项
    d = {} # 用于保存签名
    for i in range(len(w)):
        s = ''.join(sorted(w[i])) # 签名：利用sorted函数把字符串排序（易位构词的特征就是所有字母一样，只有顺序不一样，这样就可以很好的解决）
        if s in d:
            d[s].append(i) # 以下方列表的形式，记录对应的位置
        else:
            d[s] = [i]
    response = []
    for s in d:
        if len(d[s]) > 1: # 如果仅有一个位置，则说明没有易位构词
            response.append(w[i] for i in d[s]) # 做成一个generator
    return response

if __name__ == '__main__':
    w = ['le', 'chien', 'marche', 'vers', 'sa', 'niche', 'et', 'trouve', 'une', 'limace']
    response = anargams(w)