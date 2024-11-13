class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        from math import comb
        MOD = 10 ** 9 + 7
        
        dp = [k + 1] * 801
        dp[0] = k + 1
        dp[1] = 0
        
        for i in range(2, 801):
            cnt = i
            steps = 0
            while cnt != 1 and steps <= k:
                cnt = bin(cnt).count('1')
                steps += 1
            dp[i] = steps if cnt == 1 else k + 1
        
        res = 0
        left_cnt_1 = 0
        n = len(s)
        
        for i, s1 in enumerate(s):
            if s1 == "0":
                continue
            total_positions = n - i - 1
            for ones_in_rest in range(total_positions + 1):
                total_ones = left_cnt_1 + ones_in_rest
                if dp[total_ones] + 1 <= k:
                    res += comb(total_positions, ones_in_rest)
                    res %= MOD
            left_cnt_1 += 1
        
        return res % MOD
