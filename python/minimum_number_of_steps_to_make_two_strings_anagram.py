# no.1347
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        move_map = {}
        length = len(s)
        for i in range(length):
            move_map[s[i]] = move_map.get(s[i], 0) + 1
            move_map[t[i]] = move_map.get(t[i], 0) - 1
        ans = 0
        for c in move_map:
            if move_map[c] > 0:
                ans += move_map[c]
        return ans
