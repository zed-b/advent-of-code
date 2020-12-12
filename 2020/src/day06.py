import sys

def solve1(groups):
    sum = 0
    for group in groups:
        yes = set()
        for ans in group:
            for q in ans:
                yes.add(q)
        sum += len(yes)
    return sum

def solve2(groups):
    az = [chr(ord('a')+i) for i in range(26)]
    sum = 0
    for group in groups:
        yes = set(az)
        for ans in group:
            yes &= set([c for c in ans])
        sum += len(yes)
    return sum

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    inp.append('')
    groups = []
    cur = []
    for ans in inp:
        if len(ans) == 0:
            groups.append(cur)
            cur = []
            continue
        cur.append(ans)
    print(solve1(groups))
    print(solve2(groups))