# no. 779
class Solution:
    def kthGrammar(self, n: int, k:int) -> int:
        mapping = {0: [0, 1], 1: [1, 0]}
        if n == 1:
            return 0
        prev_k = self.kthGrammar(n-1, int((k+1)/2))
        if k%2:
            m = 0
        else:
            m = 1
        return mapping[prev_k][m]

if __name__ == '__main__':
    solution = Solution()
    print(solution.kthGrammar(4, 3))

