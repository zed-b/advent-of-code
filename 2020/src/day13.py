import sys,functools

def solve1(time, buses):
    best = 0
    best_at = -1
    for i,b in enumerate(buses):
        if b == 'x':
            continue
        t = int(b)
        start = t - (time % t)
        if best_at < 0 or start < best:
            best = start
            best_at = t
    return best * best_at

def modpow(base, pw, mod):
    pw %= mod
    base %= mod
    res = 1
    while(pw > 0):
        if pw & 1 > 0:
            res = (res * base) % mod
        base *= base
        pw //= 2
    return res

def crt(a,ra):
    N = functools.reduce(lambda a,b : a * b, a, 1)
    x = 0
    for i in range(len(a)):
        n = N // a[i]
        mod_others_1 = modpow(n, a[i]-2, a[i])
        x += n * mod_others_1 * ra[i]
    return x % N

def solve2(buses):
    m,r = [],[]
    for i, b in enumerate(buses):
        if b != 'x':
            a = int(b)
            m.append(a)
            r.append((a-(i%a))%a)
    return crt(m,r)

if __name__ == "__main__":
    inp = [l.rstrip() for l in sys.stdin]
    time = int(inp[0])
    buses = inp[1].split(',')
    print(solve1(time, buses))
    print(solve2(buses))