class Solution:
    def romanToInt(self, s):
        out = 0
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        dic = dict(zip(roman, values))
        if "CM" in s:
            out += dic["CM"]
            s = s.replace("CM", '')
        if "CD" in s:
            out += dic["CD"]
            s = s.replace("CD", '')
        if "XC" in s:
            out += dic["XC"]
            s = s.replace("XC", '')
        if "XL" in s:
            out += dic["XL"]
            s = s.replace("XL", '')
        if "IX" in s:
            out += dic["IX"]
            s = s.replace("IX", '')
        if "IV" in s:
            out += dic["IV"]
            s = s.replace("IV", '')
        lst = [i for i in s]
        for i in lst:
            out += dic[i]        
        return out
        # myqueue = []
        # temp_s = ''
        # j = 0
        # while j < len(lst):
        #     while len(myqueue) < 2 and j < len(lst):
        #         myqueue.append(lst[j])
        #         j += 1
        #     if len(myqueue) == 2:
        #         temp_s = myqueue[0] + myqueue[1]
        #     else:
        #         temp_s = myqueue[0]
        #     if temp_s not in dic:
        #         out += dic[myqueue.pop(0)]
        #     else:
        #         out += dic[temp_s]
        #         myqueue = []
    def shortRomanToInt(self, s):
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        outint, p = 0, 'I'
        for c in s[::-1]: # 从后往前读，遇到比当前值小则减，大则加
            outint, p = outint - d[c] if d[c] < d[p] else outint + d[c], c
        return outint
            
if __name__ == '__main__':
    s = 'III'
    solu = Solution()
    r_int = solu.romanToInt(s)
    print(r_int)
