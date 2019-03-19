'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.
'''


class Solution:
    def isValid(self, s):
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            elif i == ')' or i == ']' or i == '}':
                if len(stack) > 0:
                    temp_parent = ''
                    temp_parent = stack[-1] + i
                else: 
                    return False
                if temp_parent == '()' or temp_parent == '[]' or temp_parent == '{}':
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False