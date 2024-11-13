class Solution:
    def sumOfGoodSubsequences(self, nums):
        MOD = 10 ** 9 + 7
        hash_set = {}

        for num in nums:
            num_add, num_sub = num + 1, num - 1
            s_add, c_add = hash_set.get(num_add, (0, 0))
            s_sub, c_sub = hash_set.get(num_sub, (0, 0))
            s_num, c_num = hash_set.get(num, (0, 0))

            new_sum = (s_add + s_sub + s_num + num * (c_add + c_sub + 1)) % MOD
            new_count = (c_add + c_sub + c_num + 1) % MOD

            hash_set[num] = (new_sum, new_count)

        res = sum(s for s, c in hash_set.values()) % MOD
        return res
