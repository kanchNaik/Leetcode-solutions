class Solution:
    def intToRoman(self, num: int) -> str:
        int_rom_map_vals ={ 'M' : 1000  ,  'CM': 900 ,  'D': 500 ,  'CD': 400 ,  'C': 100 ,  'XC': 90 ,  'L': 50 ,  'XL': 40 ,  'X': 10 ,  'IX': 9 ,  'V': 5 ,  'IV': 4 ,  'I': 1}
        rom=''
        for k,v in int_rom_map_vals.items():
            q=num//v
            num=num%v
            rom+=(q*k)
        return rom
        