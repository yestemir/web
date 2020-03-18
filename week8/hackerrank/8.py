if __name__ == '__main__':

    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    from operator import itemgetter

    s = set()
    #l.sort(key=itemgetter(1))
    for i in l:
        s.add(i[1])