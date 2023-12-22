#no. 1422
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        ones = []
        for i, c in enumerate(s[-1]):
            if c == '1':
                ones.append(i)
        ones.append(len(s) - 1)
        for i, j in enumerate(ones):
            if j == 0:
                continue
            right_score = len(ones) - i
            if s[-1] == '0':
                right_score -= 1
            left_score = j - i 
            total_score = right_score + left_score
            print(right_score, left_score)
            if total_score > max_score:
                max_score = total_score
        return max_score
