# no. 1277
class Solution(object):
    def countSquares(self, matrix):
        square = 0
        h = len(matrix)
        w = len(matrix[0])
        dp = [[0 for i in range(w)] for j in range(h)]
        dp[0] = matrix[0]
        square += sum(dp[0])

        for i in range(1, h):
            dp[i][0] = matrix[i][0]
            square += matrix[i][0]
       # print(dp)

        for i in range(1, h):
            for j in range(1, w):
                previous_states = [dp[i-1][j], dp[i][j-1], dp[i-1][j-1]] #up, left, up left 
                if matrix[i][j]:
                    dp[i][j] = 1 + min(previous_states)
                    square += dp[i][j]

        return square

def print_matrix(matrix):
    h = len(matrix)
    for i in range(h):
        print(matrix[i])  


if __name__ == "__main__":
    sol = Solution()
    M1 = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
    print('M1')
    print_matrix(M1)
    ans1 = sol.countSquares(M1)
    #print('DP1:')
    #print_matrix(ans1[0])
    print(ans1)
    M2 = [[1,0,1],[1,1,0],[1,1,0]]
    print('M2:')
    print_matrix(M2)
    ans2 = sol.countSquares(M2)
    #print('DP2:')
    #print_matrix(ans2[0])
    print(ans2)
