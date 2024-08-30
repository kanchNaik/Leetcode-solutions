class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # dict_s = {}
        # dict_t = {}
        # i = j = 0
        # m = len(s)
        # n = len(t)

        # if(m != n):
        #     return False

        # while(i < m):
        #     if(s[i] in dict_s):
        #         dict_s[s[i]].append(i)
        #     else:
        #         dict_s[s[i]] = [i]

        #     if(t[i] in dict_t):
        #         dict_t[t[i]].append(i)
        #     else:
        #         dict_t[t[i]] = [i]
            
        #     i += 1

        # print(dict_s)
        # print(dict_t)
        # s_index = list(dict_s.values())
        # t_index = list(dict_t.values())
    
        # return s_index == t_index
        dict_s = {}
        dict_t = {}
        i = 0
        m = len(s)
        n = len(t)

        if(m != n):
            return False

        while(i < m):
            if(s[i] in dict_s or t[i] in dict_t):
                if(s[i] in dict_s and t[i] in dict_t and dict_s[s[i]] == dict_t[t[i]]):
                        dict_s[s[i]].append(i)
                        dict_t[t[i]].append(i)
                else:
                    break
            else:
                dict_s[s[i]] = [i]
                dict_t[t[i]] = [i]

            i += 1
    
        return i == m
    
sol = Solution()
val = sol.isIsomorphic('aaaa', 'aaaa')
print(val)

            


        
