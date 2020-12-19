import sys

def solve1(nums, D):
    for i in range(D, len(nums)):
        ok = False
        for a in range(i-D, i):
            for b in range(a+1, i):
                if nums[a] + nums[b] == nums[i]:
                    ok = True
        if not ok:
            return nums[i]
    return -1

def solve2(nums, need):
    for i in range(len(nums)):
        sum = nums[i]
        for j in range(i+1, len(nums)):
            sum += nums[j]
            if sum == need:
                return min(nums[i:j+1]) + max(nums[i:j+1])

if __name__ == "__main__":
    nums = [int(l.rstrip()) for l in sys.stdin]
    # take care if sample or not
    D = 5 if '--sample' in sys.argv else 25
    ans = solve1(nums, D)
    print(ans)
    print(solve2(nums, ans))
