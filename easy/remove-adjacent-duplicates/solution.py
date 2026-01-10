class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TODO: Write your code here
        # Using a stack is the easiest solution here
        stack = []
        for c in s:
            if stack and c == stack[-1]: # check if stack exists, and the top is 'c'
                stack.pop() # if yes, pop
            else:
                stack.append(c) # or push
        return "".join(stack) # return stack elements joined