import sys

def solve(nums, last):
    seen = {}
    prev = -1
    for i in range(last):
        cur = -1
        if i < len(nums):
            cur = nums[i]
        else:
            last, diff = seen[prev]
            cur = diff

        if cur in seen:
            seen[cur] = (i, i-seen[cur][0])
        else:
            seen[cur] = (i, 0)

        prev = cur

    return prev

def solve1(nums):
    return solve(nums, 2020)

def solve2(nums):
    # smaller n for sample check
    N = 300000 if '--sample' in sys.argv else 30000000
    return solve(nums, N)

if __name__ == "__main__":
    nums = list(map(int, [l for l in sys.stdin][0].split(',')))
    print(solve1(nums))
    print(solve2(nums))