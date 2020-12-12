import sys

def solve1(boxes):
    return sum(map(lambda x : x[0]*x[1]*3 + x[1]*x[2]*2 + x[2]*x[0]* 2, boxes))

def solve2(boxes):
    return sum(map(lambda x : x[0]*x[1]*x[2] + x[0]*2 + x[1]*2, boxes))

if __name__ == "__main__":
    boxes = [sorted(list(map(int,l.split('x')))) for l in sys.stdin ]
    print(solve1(boxes))
    print(solve2(boxes))