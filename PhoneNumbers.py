def sanitizeString(s):
    return s.replace("-", "").replace(" ", "")


def partition(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]


def processString(s):
    s = sanitizeString(s)
    x = ""
    if len(s) % 3 == 0:
        p = partition(s, 3)
    elif len(s) % 3 == 2:
        p = partition(s[:len(s) - 2], 3)
        p.append(s[-2:])
    else:
        p = partition(s[:len(s) - 4], 3)
        y = partition(s[-4:], 2)
        p = p + y

    for _ in p:
        x = x + _ + "-"
    return x[:-1]


if __name__ == "__main__":
    print(processString("40409422"))
    print(processString("404098422"))
    print(processString("342"))
    print(processString("3428"))
    print(processString("342-18"))
    print(processString("9 3492-18"))
    print(processString("-----"))
    print(processString(""))
    print(processString(" "))
