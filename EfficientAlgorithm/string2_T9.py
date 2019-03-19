t9 = "22233344455566677778889999" # 分别对应abc def ghi jkl mno pqrs tuv wxyz

def letter_digit(x):
    assert 'a' <= x <= 'z' # assert(断言)，对则通过，不对则抛出错误
    return t9[ord(x)-ord('a')] # 取ASCII码，做差找到t9按键的对应位置

def word_code(words):
    return ''.join(map(letter_digit, words)) # map函数将前参数（另一个函数），应用到后一个参数（列表中）的每一个上

def predictive_text(dic):
    freq = {}
    for words, weights in dic:
        prefix = ""
        for x in words:
            if prefix in freq:
                freq[prefix] += weights
            else:
                freq[prefix] = weights
    prop = {}
    for prefix in freq:
        code = word_code(prefix)
        if code not in prop or freq[prop[code]] < freq[prefix]:
            prop[code] = prefix
    return prop

def propose(prop, seq):
    if seq in prop:
        return prop
    else:
        return "None"

# if __name__ == '__main__':
