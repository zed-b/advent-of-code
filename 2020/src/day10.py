import sys

def solve1(nums):
    diff = dict({1:0,2:0,3:0})
    for i in range(1, len(nums)):
        diff[nums[i]-nums[i-1]] += 1
    return diff[1] * diff[3]

def solve2(nums):
    ways = [0] * (nums[-1] + 1)
    ways[0] = 1
    for i in range(1, len(nums)):
        a = nums[i]
        for j in range(max(0, a-3), a):
            ways[a] += ways[j]
    return ways[-1]

if __name__ == "__main__":
    nums = [int(l.rstrip()) for l in sys.stdin]
    nums.append(max(nums)+3)
    nums.append(0)
    nums.sort()
    print(solve1(nums))
    print(solve2(nums))
