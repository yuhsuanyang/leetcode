# no.343

class Solution:
    def product(self, nums):
        result = 1
        for i in nums:
            result *= i
        return result

    def integerBreak(self, n: int) -> int:
        best_sum = {1: [1], 2: [1, 1]}
        if n == 2:
            return 1
        def get_decomposed(nums):
            results = []
            for j in range(len(nums)):
                results.append(nums[:j] + best_sum[can[j]] + can[j+1:])
            return results

        for i in range(3, n+1):
            last_state = best_sum[i-1]
            max_product = 1
            for j in range(len(last_state)):
                can = last_state.copy()
                can[j] += 1
                if self.product(can) > max_product:
                    max_product = self.product(can)
                    selected = can
                    decomposed_can = get_decomposed(can)
                    for can in decomposed_can:
                        if self.product(can) >= max_product:
                            selected = can
                    candidate_list = selected
            best_sum[i] = candidate_list

        print(best_sum)

if __name__ == '__main__':
    sol = Solution()
    sol.integerBreak(58)

                    
