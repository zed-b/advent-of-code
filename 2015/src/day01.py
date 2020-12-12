import sys

def solve1(inst):
    floor = 0
    for c in inst:
        floor += c == '('
        floor -= c == ')'
    return floor

def solve2(inst):
    floor = 0
    for i in range(len(inst)):
        floor += inst[i] == '('
        floor -= inst[i] == ')'
        if floor == -1:
            return i + 1
    return -1

if __name__ == "__main__":
    inst = [l.rstrip() for l in sys.stdin][0]
    print(solve1(inst))
    print(solve2(inst))