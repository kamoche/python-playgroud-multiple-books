def birthday(s, d, m):
    # Write your code here
    ways = 0
    if s:
        for x in range(len(s)):
            seg = 1
            total = s[x]
            while seg <= m:
                if total == d and seg == m:
                    ways += 1
                    break
                elif total < d and (x + seg) < len(s):
                    total += s[x + seg]
                    seg += 1
                else:
                    seg += 1


    return ways
