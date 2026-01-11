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

# Testing the algorithm with example inputs
def assert_test(got, expected):
	print("Result :", got, " Expected: ", expected)
	assert got == expected
	assert type(got) is type(expected)

if __name__ == "__main__":
    solution = Solution()
    assert_test(solution.removeDuplicates("abccba"), "") # Output: ""
    assert_test(solution.removeDuplicates("foobar"), "fbar") # Output: "fbar"
    assert_test(solution.removeDuplicates("abcd"), "abcd") # Output: "abcd"

    print("\033[92m[OK]\033[0m All test cases passed")
