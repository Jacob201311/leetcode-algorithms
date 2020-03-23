"""
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.



Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]


Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
"""

class Solution:

    """
	cost: 900 ms > 96.55%
	memroy: > 100%
	https://leetcode.com/submissions/detail/315134920/
    """
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # init n + 1 array, and the last value is used for mark
        result = [0] * (n + 1)

        for booking in bookings:
            # marking interval head
            result[booking[0] - 1] += booking[2]
            # marking interval tail(means tail + 1 positon)
            result[booking[1]] -= booking[2]

        for x in range(1, n):
            # since we know every interval,
            # so just rolling update the value in the interval
            result[x] += result[x -1]

        return result[:-1]
