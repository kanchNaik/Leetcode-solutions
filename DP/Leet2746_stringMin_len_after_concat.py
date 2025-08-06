from math import inf

def join(len1, f1, l2, len2):
    if f1 == l2:
        return len1 + len2 -1
    else:
        return len1 + len2

def MinimumLength(words):
    n = len(words)

    dp = [[(inf, '', '') for _ in range(2)] for _ in range(n)]

    dp[0][0] = (len(words[0]), words[0][0], words[0][-1])

    for i in range(1, n):
        for j in range(2):
            prev_len, f1, l1 = dp[i - 1][j]

            new_len_0 = join(prev_len, l1, words[i][0], len(words[i]))
            if(dp[i][0][0] > new_len_0):
                dp[i][0] = (new_len_0, f1, words[i][-1])
            
            new_len_1 = join(prev_len, f1, words[i][-1], len(words[i]))

            if(dp[i][1][0] > new_len_1):
                dp[i][1] = (new_len_1, words[i][0], l1)

    return min(dp[n - 1][0][0], dp[n - 1][1][0])


words = ["aab","abc","aac","b"]
print(MinimumLength(words))
