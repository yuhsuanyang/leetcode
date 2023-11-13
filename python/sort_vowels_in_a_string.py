# no.2785

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_pos = []
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        char_list, vs = [], []
        for i, c in enumerate(s):
            char_list.append(c)
            if c in vowels:
                vowels_pos.append(i)
                vs.append(c)
                
        if len(vs):
            vs.sort()
            for i, j in enumerate(vowels_pos):
                char_list[j] = vs[i]
        s = ''.join(char_list)
        return s
        

