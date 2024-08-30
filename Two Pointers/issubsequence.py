import numpy as np

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m = len(t)
        n = len(s)

        if(m < n):
            return False
        
        i = 0
        j = 0
        map_t = {}

        while(j < m):
            if(t[j] in map_t):
                map_t[t[j]].append(j)
            else:
                map_t[t[j]] = [j] 
            j += 1

        print(map_t)

        prev = -1
        while(i < n):
            if(s[i] in map_t):
                indexs = map_t[s[i]]
                print(indexs)
                index_val = [i for i in indexs if i > prev]
                if(len(index_val) > 0):
                    prev = index_val[0]
                else:
                    break
                
                i += 1
            else:
                break

        return i == n

sol = Solution()
val = sol.isSubsequence('acc', 'ahbgdca')   
print(val)