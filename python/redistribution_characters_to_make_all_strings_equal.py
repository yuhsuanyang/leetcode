#no. 1897

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_dict = {}
        for w in words:
            for c in w:
                char_dict[c] = char_dict.get(c, 0) + 1
        for c in char_dict:
            if char_dict[c] % len(words):
                return False
        return True

