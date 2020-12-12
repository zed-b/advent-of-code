import sys

def solve1(nums):
    return max(nums)

def solve2(nums):
    cur = min(nums)
    has = set(nums)
    while True:
        if cur not in has:
            return cur
        cur += 1

if __name__ == "__main__":
    nums = []
    for l in sys.stdin:
        l = l.rstrip()
        cur = 0
        for c in l:
            cur <<= 1
            cur += (c == 'B' or c == 'R')
        nums.append(cur)
    print(solve1(nums))
    print(solve2(nums))
