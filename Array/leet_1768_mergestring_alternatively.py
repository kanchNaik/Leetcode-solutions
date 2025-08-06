class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        n = len(word1)
        m = len(word2)
        word3 = ''
        i= 0
        while i < n and i < m:
            word3 += word1[i] + word2[i]
            i +=1
        
        while i < n:
            word3 += word1[i]
            i+=1

        while i< m:
            word3 += word2[i]
            i+=1

        return word3