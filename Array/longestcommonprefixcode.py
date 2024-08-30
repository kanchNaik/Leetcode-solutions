from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = list()

        sortedstrings = sorted(strs)
        first_string = sortedstrings[0]
        last_string = sortedstrings[len(strs) - 1]

        index = 0

        while(index < len(first_string) and index < len(last_string)):
            if (first_string[index] == last_string[index]):
                pref.append(first_string[index])
                index += 1
            else:
                break;
                
        return ''.join(pref)
        