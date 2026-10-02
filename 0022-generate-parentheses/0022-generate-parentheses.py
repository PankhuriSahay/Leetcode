class Solution(object):
    def generateParenthesis(self, n):
        ans = []

        def backtrack(s, opening, closing):
            # We have used all n pairs
            if len(s) == 2 * n:
                ans.append(s)
                return

            # Add '(' if we still have some left
            if opening < n:
                backtrack(s + "(", opening + 1, closing)

            # Add ')' only when it can match an opening bracket
            if closing < opening:
                backtrack(s + ")", opening, closing + 1)

        backtrack("", 0, 0)

        return ans