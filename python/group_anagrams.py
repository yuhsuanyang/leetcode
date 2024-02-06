#no. 49
class Solution:
    def __init__(self):
        self.dict = {c: str(i) for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}

    def encode(self, s):
        seq = []
        for c in s:
            seq.append(self.dict[c])
        seq.sort()
        return ' '.join(seq)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            encoded = self.encode(s)
            if encoded in anagrams:
                anagrams[encoded].append(s)
            else:
                anagrams[encoded] = [s]
        ans = []
        for key in anagrams:
            ans.append(anagrams[key])
        return ans
