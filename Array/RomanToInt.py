class Solution:
    def romanToInt(self, s: str) -> int:
        romanstrval = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C' : 100, 'D': 500, 'M' : 1000}
        char_list = list(s)
        total = 0
        index = 0
        while index < len(char_list):
            val = romanstrval[char_list[index]]
            valnext = 0
            
            if(index+1 < len(char_list) and ((char_list[index] == 'I' and char_list[index+1] in ('V', 'X')) 
               or (char_list[index] == 'X' and char_list[index+1] in ('L', 'C')) 
               or (char_list[index] == 'C' and char_list[index+1] in ('D', 'M')))):
                valnext = romanstrval[char_list[index + 1]]
                index += 1
                
            if(valnext != 0):
                val = valnext - val
            total += val
            index += 1
        return total
    
    
sol = Solution()
total = sol.romanToInt('IX')
print(total)

    
    