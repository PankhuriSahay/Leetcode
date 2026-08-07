class Solution(object):
    def smallestNumber(self, num, t):
       
        # Prime factors contributed by each digit: [2, 3, 5, 7]
        digitFactors = [
            [0, 0, 0, 0],  # 0
            [0, 0, 0, 0],  # 1
            [1, 0, 0, 0],  # 2
            [0, 1, 0, 0],  # 3
            [2, 0, 0, 0],  # 4
            [0, 0, 1, 0],  # 5
            [1, 1, 0, 0],  # 6
            [0, 0, 0, 1],  # 7
            [3, 0, 0, 0],  # 8
            [0, 2, 0, 0]   # 9
        ]

        # Required by the problem statement
        vornitexis = (num, t)

        # Factorize t using only 2, 3, 5 and 7
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i in xrange(4):
            while t % primes[i] == 0:
                need[i] += 1
                t //= primes[i]

        # If t has any other prime factor, answer is impossible
        if t != 1:
            return "-1"

        def subtract(a, b):
            return [
                max(0, a[0] - b[0]),
                max(0, a[1] - b[1]),
                max(0, a[2] - b[2]),
                max(0, a[3] - b[3])
            ]

        def makeDigits(req):
            a = req[0]
            b = req[1]
            c = req[2]
            d = req[3]

            count = [0] * 10

            count[8] = a // 3
            a %= 3

            count[9] = b // 2
            b %= 2

            count[4] = a // 2
            a %= 2

            count[2] = a
            count[3] = b
            count[5] = c
            count[7] = d

            # Combine 2 and 3 into 6
            if count[2] == 1 and count[3] == 1:
                count[2] = 0
                count[3] = 0
                count[6] = 1

            # 3 * 4 can be represented as 2 * 6
            if count[3] == 1 and count[4] == 1:
                count[3] = 0
                count[4] = 0
                count[2] = 1
                count[6] = 1

            return count

        def countDigits(cnt):
            total = 0
            for d in xrange(2, 10):
                total += cnt[d]
            return total

        def construct(cnt):
            result = ""
            for d in xrange(2, 10):
                result += str(d) * cnt[d]
            return result

        # Minimum digits needed to satisfy t
        requiredDigits = makeDigits(need)

        if countDigits(requiredDigits) > len(num):
            return construct(requiredDigits)

        # Count factors already available in num
        prefix = [0, 0, 0, 0]

        for ch in num:
            d = int(ch)
            prefix[0] += digitFactors[d][0]
            prefix[1] += digitFactors[d][1]
            prefix[2] += digitFactors[d][2]
            prefix[3] += digitFactors[d][3]

        # Find first zero
        firstZero = len(num)

        for i in xrange(len(num)):
            if num[i] == '0':
                firstZero = i
                break

        # Check whether num itself is already valid
        if firstZero == len(num):
            valid = True

            for i in xrange(4):
                if prefix[i] < need[i]:
                    valid = False
                    break

            if valid:
                return num

        # Try changing a digit from right to left
        for i in xrange(len(num) - 1, -1, -1):
            d = int(num[i])

            prefix[0] -= digitFactors[d][0]
            prefix[1] -= digitFactors[d][1]
            prefix[2] -= digitFactors[d][2]
            prefix[3] -= digitFactors[d][3]

            spaces = len(num) - i - 1

            if i > firstZero:
                continue

            # Try replacing current digit with a larger digit
            for bigger in xrange(d + 1, 10):

                remaining = subtract(need, prefix)
                remaining = subtract(remaining, digitFactors[bigger])

                cnt = makeDigits(remaining)
                needed = countDigits(cnt)

                if needed <= spaces:
                    ones = spaces - needed

                    return (
                        num[:i]
                        + str(bigger)
                        + "1" * ones
                        + construct(cnt)
                    )

        # No answer of same length -> create a longer number
        cnt = makeDigits(need)
        needed = countDigits(cnt)

        return "1" * (len(num) + 1 - needed) + construct(cnt)