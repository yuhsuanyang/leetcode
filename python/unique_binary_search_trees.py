# no. 96
class Solution(object):
    def numTrees(self, n):
        trees = [1]*(n+1) # n=0,1, trees = 1

        for i in range(2, n+1):
            total_trees = 0
            for j in range(0, i):
                total_trees += trees[j]*trees[i-1-j]
            trees[i] = total_trees
        return trees[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.numTrees(3)) # 5
    print(solution.numTrees(4)) # 14
    


