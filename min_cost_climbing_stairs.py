"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:

    def __init__(self):
        self.lengthMinCostDict = {}

    """
	cost: 196 ms > 5.44
	memory: < 7.69
	https://leetcode.com/submissions/detail/314796060/
	not good due to the recrusive relations expression not use list index as the variable
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(n) = min(f(n-1) + cost[-1], f(n-1) + cost[-2])
        if not cost:
            return 0

        if (len(cost) in self.lengthMinCostDict):
            return self.lengthMinCostDict[len(cost)]

        if len(cost) <= 2:
            if len(cost) == 1:
                return 0
            return min(cost[0], cost[1])

        minCost =  min(self.minCostClimbingStairs(cost[:-1]) + cost[-1],
                   self.minCostClimbingStairs(cost[:-2]) + cost[-2])
        self.lengthMinCostDict[len(cost)] = minCost
        return minCost
