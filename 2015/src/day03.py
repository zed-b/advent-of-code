import sys

def visited_houses(inst):
    x, y = 0, 0
    vis = set([(x,y)])
    for c in inst:
        if c == ">":
            x += 1
        elif c == "<":
            x -= 1
        elif c == "v":
            y += 1
        elif c == "^":
            y -= 1
        vis.add((x,y))
    return vis

def solve1(inst):
    return len(visited_houses(inst))

def solve2(inst):
    return len(visited_houses([inst[i] for i in range(len(inst)) if i % 2 == 0 ]) | \
               visited_houses([inst[i] for i in range(len(inst)) if i % 2 == 1 ]))

if __name__ == "__main__":
    inst = [l for l in sys.stdin][0].rstrip()
    print(solve1(inst))
    print(solve2(inst))


