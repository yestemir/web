if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    max = -1000000
    for i in arr:
        if i > max:
            max = i

    for i in arr:
        if i == max:
            i = -1

    for i in arr:
        print(i)


    print(max)