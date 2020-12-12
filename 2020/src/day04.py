import sys, re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def solve1(passports):
    ans = 0
    for p in passports:
        cur = set()
        for kv in p:
            if (kv[0] in fields):
                cur.add(kv[0])
        if len(cur) == len(fields):
            ans += 1
    return ans

def solve2(passports):
    ans = 0
    for p in passports:
        cur = set()
        for k, v in p:
            if k not in fields:
                continue
            ok = False
            if k == "byr":
                ok = int(v) and 1920 <= int(v) and int(v) <= 2002
            if k == "iyr":
                ok = int(v) and 2010 <= int(v) and int(v) <= 2020
            if k == "eyr":
                ok = int(v) and 2020 <= int(v) and int(v) <= 2030
            if k == "hgt":
                if v[-2:] == "cm":
                    m = v[:-2]
                    ok = int(m) and 150 <= int(m) and int(m) <= 193
                if v[-2:] == "in":
                    m = v[:-2]
                    ok = int(m) and 56 <= int(m) and int(m) <= 76
            if k == "ecl":
                ok = v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if k == "pid":
                r = re.search(r"^([0-9]){9}$", v)
                ok = r is not None
            if k == "hcl":
                r = re.search(r"^#([a-f0-9]){6}$", v)
                ok = r is not None

            if ok:
                cur.add(k)
            else:
                cur.clear()
                break

        if len(cur) == len(fields):
            ans += 1
    return ans

if __name__ == "__main__":
    passports = []
    inp = [l.strip() for l in sys.stdin]
    inp.append('')
    cur = []
    for l in inp:
        if len(l) == 0:
            passports.append(cur)
            cur = []
            continue
        r = re.findall(r"(\w+):(\S+)", l)
        for kv in r:
            ok = False
            cur.append((kv[0],kv[1]))
    print(solve1(passports))
    print(solve2(passports))