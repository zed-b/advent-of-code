import sys

def solve1(nums, need):
    prev = set()
    for a in nums:
        if need - a in prev:
            return a * (need - a)
        prev.add(a)

def solve2(nums, need):
    twosum = dict()
    for i in range(len(nums)):
        if need - nums[i] in twosum:
            return nums[i] * twosum[need - nums[i]]
        for j in range(i):
            twosum[nums[i] + nums[j]] = nums[i] * nums[j]

if __name__ == "__main__":
    nums = [int(a) for a in sys.stdin]
    need = 2020
    print(solve1(nums, need))
    print(solve2(nums, need))