import sys

def simulate(code, change_at=-1):
    vis = set()
    at, acc = 0, 0
    while (True):
        if at >= len(code) or at in vis:
            return (at, acc)
        vis.add(at)

        inst,val = code[at]

        if change_at == at:
            if inst == "nop":
                inst = "jmp"
            elif inst == "jmp":
                inst = "nop"

        if inst == "nop":
            at += 1
            continue
        elif inst == "acc":
            at += 1
            acc += val
        else:
            at += val

def solve1(code):
    return simulate(code)[1]

def solve2(code):
    for i in range(len(code)):
        at,acc = simulate(code,i)
        if at >= len(code):
            return acc

if __name__ == "__main__":
    code = [(line[:3], int(line[4:])) for line in sys.stdin]
    print(solve1(code))
    print(solve2(code))



