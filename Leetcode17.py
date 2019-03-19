'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.
'''
class Solution:
    def letterCombinations(self, digits):
        phone_dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        output = []

        def backtrack(combination, next_digit):
            if len(next_digit) == 0:
                output.append(combination)
            else:
                for letter in phone_dic[next_digit[0]]:
                    backtrack(combination+letter, next_digit[1:])
        
        if digits:
            backtrack("", digits)
        return output

if __name__ == '__main__':
    digits = "234"
    solu = Solution()
    output = solu.letterCombinations(digits)
    print(output)