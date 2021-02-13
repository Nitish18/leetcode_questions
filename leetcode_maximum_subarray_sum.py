from typing import List
from copy import deepcopy

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        s = float('-inf')
        ans_subarray = []

        j = 0
        while(True):
            if j == n:
                return (sum(ans_subarray), ans_subarray)
            i = j
            loop_finished = False
            skip_this = False
            while(True):
                if i == n:
                    loop_finished = True
                    break
                t = sum(nums[j:i])
                if (t+nums[i]) >= s:
                    s = t
                    ans_subarray = deepcopy(nums[j:i+1])
                    i = i + 1
                elif (t+nums[i]) < 0:
                    j = i + 1
                    skip_this = True
                    break
                else:
                    i = i + 1
            if loop_finished:
                return (sum(ans_subarray), ans_subarray)
            elif skip_this:
                pass
            else:
                j = j + 1
