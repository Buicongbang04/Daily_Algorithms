'''
2338. Count the Number of Ideal Arrays
Solved
Hard
Topics
Companies
Hint
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

Constraints:

2 <= n <= 104
1 <= maxValue <= 104
'''
# link: https://leetcode.com/problems/count-the-number-of-ideal-arrays
# class Solution(object):
    # def idealArrays(self, n, maxValue):
    #     count = self.find_devided(maxValue)
    #     if n == 2: return count
    #     return (count + maxValue + n - 2)
    # def find_devided(self, maxValue):
    #     temp = 0
    #     count = 0
    #     while temp != maxValue:
    #         temp += 1
    #         for i in range(1, temp + 1):
    #             if temp % i == 0:
    #                 print(temp)
    #                 count += 1
    #     return count

LIMIT = 10**9 + 7

class Solution:
    def idealArrays(self, n, maxValue):
        max_len = 14  
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % LIMIT
        
        inv_fact[n] = pow(fact[n], LIMIT - 2, LIMIT)
        for i in range(n - 1, 0, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % LIMIT
        
        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fact[a] * inv_fact[b] % LIMIT * inv_fact[a - b] % LIMIT

        ideal_count = [{} for _ in range(max_len + 1)]
        for i in range(1, maxValue + 1):
            ideal_count[1][i] = 1

        for length in range(1, max_len):
            for num in ideal_count[length]:
                count = ideal_count[length][num]
                for mult in range(num * 2, maxValue + 1, num):
                    ideal_count[length + 1][mult] = ideal_count[length + 1].get(mult, 0) + count
                    if ideal_count[length + 1][mult] >= LIMIT:
                        ideal_count[length + 1][mult] -= LIMIT

        res = 0
        for length in range(1, max_len + 1):
            for val in ideal_count[length]:
                count = ideal_count[length][val]
                res += count * comb(n - 1, length - 1)
                res %= LIMIT
        return res

        