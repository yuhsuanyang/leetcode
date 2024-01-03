# no. 2125
class Solution:
    def count_lights(self, s):
        count = 0
        for c in s:
            if c == '1':
                count += 1
        return count

    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        top = 0
        down = 0
        for row in bank:
            n_row_lights = self.count_lights(row)
            if n_row_lights:
                if top == 0:
                    top = n_row_lights
                elif down == 0:
                    down = n_row_lights
                    ans += top * down
                    top = down
                    down = 0
        return ans

