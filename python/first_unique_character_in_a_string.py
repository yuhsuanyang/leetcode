#no. 387
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {c: [] for c in 'abcdefghijklmnopqrstuvwxyz'}
        for i in range(len(s)):
            counter[s[i]].append(i)
        first_index = len(s)
        for c in counter:
            if len(counter[c]) == 1:
                if counter[c][0] < first_index:
                    first_index = counter[c][0]
        return -1 if first_index == len(s) else first_index
