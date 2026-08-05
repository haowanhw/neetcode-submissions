class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from the right of the deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) # append adds element to the right of the deque (appendleft)

            # remove the left value from the window
            if l > q[0]:
                q.popleft()

            # check if window is complete and add max to output
            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

        