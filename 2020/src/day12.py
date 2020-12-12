import sys, math

def solve1(nav):
    x,y,ang = 0,0,0
    for dir,val in nav:
        if dir == "N":
            y += val
        elif dir == "S":
            y -= val
        elif dir == "E":
            x += val
        elif dir == "W":
            x -= val
        elif dir == "F":
            x += val * math.cos(ang)
            y += val * math.sin(ang)
        elif dir == "L":
            ang += math.radians(val)
        elif dir == "R":
            ang -= math.radians(val)

    return round(abs(x) + abs(y))

def solve2(nav):
    sx,sy = 0, 0
    wx,wy = 10, 1
    for dir,val in nav:
        if dir == "N":
            wy += val
        elif dir == "S":
            wy -= val
        elif dir == "E":
            wx += val
        elif dir == "W":
            wx -= val
        elif dir == "F":
            sx += val*wx
            sy += val*wy
        elif dir == "L":
            r = math.radians(val)
            wx, wy = wx * math.cos(r) - wy * math.sin(r), wx * math.sin(r) + wy * math.cos(r)
        elif dir == "R":
            r = -math.radians(val)
            wx, wy = wx * math.cos(r) - wy * math.sin(r), wx * math.sin(r) + wy * math.cos(r)

    return round(abs(sx) + abs(sy))

if __name__ == "__main__":
    nav = [(l[0],int(l[1:])) for l in sys.stdin]
    print(solve1(nav))
    print(solve2(nav))
