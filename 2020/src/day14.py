import sys,re

def solve1(inp):
    vals = {}
    mask = ""
    for l in inp:
        if l[1] == "a":
            match = re.search(r"([01X]+)", l)
            mask = match[1][::-1]
        else:
            match = re.search(r"(\d+)[^\d]+(\d+)", l)
            addr, val = int(match[1]), int(match[2])
            real_val = 0
            for i in range(len(mask)):
                if mask[i] == 'X':
                    real_val += ((val >> i) & 1) << i
                else:
                    real_val += int(mask[i]) << i
            vals[addr] = real_val
    return sum((v for v in vals.values()))

def solve2(inp):
    def gen_addr(val, mask, at, res, addresses):
        if at == len(mask):
            addresses.append(res)
        else:
            if mask[at] == 'X':
                gen_addr(val, mask, at+1, res + (1<<at), addresses)
                gen_addr(val, mask, at+1, res, addresses)
            elif mask[at] == '1':
                gen_addr(val, mask, at+1, res + (1<<at), addresses)
            else:
                gen_addr(val, mask, at+1, res + (((val>>at) & 1)<<at), addresses)

    vals = {}
    mask = ""
    for l in inp:
        if l[1] == "a":
            match = re.search(r"([01X]+)", l)
            mask = match[1][::-1]
        else:
            match = re.search(r"(\d+)[^\d]+(\d+)", l)
            addr, val = int(match[1]), int(match[2])
            addresses = []
            gen_addr(addr, mask, 0, 0, addresses)
            for addr in addresses:
                vals[addr] = val
    return sum((v for v in vals.values()))

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    print(solve1(inp))
    print(solve2(inp))