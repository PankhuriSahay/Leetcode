class Solution(object):
    def evaluate(self, s, knowledge):
        d = {}

        # Convert knowledge into dictionary
        for key, value in knowledge:
            d[key] = value

        ans = ""
        i = 0

        while i < len(s):
            if s[i] == '(':
                i += 1
                key = ""

                # Collect everything until ')'
                while s[i] != ')':
                    key += s[i]
                    i += 1

                # Replace key with its value
                if key in d:
                    ans += d[key]
                else:
                    ans += "?"

            else:
                ans += s[i]

            i += 1

        return ans