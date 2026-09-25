class Solution(object):
    def braceExpansionII(self, expression):
        def combine(a, b):
            return {x + y for x in a for y in b}

        def parse(s):
            groups = []
            current = {""}
            i = 0

            while i < len(s):
                if s[i] == '{':
                    j = i
                    count = 0

                    while j < len(s):
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1

                        if count == 0:
                            break
                        j += 1

                    inside = parse(s[i + 1:j])
                    current = combine(current, inside)
                    i = j + 1

                elif s[i] == ',':
                    groups.append(current)
                    current = {""}
                    i += 1

                else:
                    current = combine(current, {s[i]})
                    i += 1

            groups.append(current)

            result = set()
            for group in groups:
                result |= group

            return result

        return sorted(parse(expression))