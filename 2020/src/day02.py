import sys, re

def solve1(vals):
    sum = 0
    for res in vals:
        cnt = 0
        i = int(res[1])
        j = int(res[2])
        for c in res[4]:
            if c == res[3]:
                cnt += 1
        if cnt >= int(res[1]) and cnt <= int(res[2]):
            sum += 1
    return sum

def solve2(vals):
    sum = 0
    for res in vals:
        i = int(res[1])
        j = int(res[2])
        cnt = 0
        if res[4][i-1] == res[3]:
            cnt += 1
        if res[4][j-1] == res[3]:
            cnt += 1
        if cnt == 1:
            sum += 1
    return sum

if __name__ == "__main__":
    vals = [re.search(r"(\d+)-(\d+) (\w): (\w+)", line) for line in sys.stdin]
    print(solve1(vals))
    print(solve2(vals))

