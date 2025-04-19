N = int(input())

def bt(cur):
    answer.append(int(cur))
    for j in range(0, int(cur[-1])):
        bt(cur + str(j))


if N > 1023:
    print(-1)
else:
    answer = []
    for i in range(10):
        bt(str(i))

    print(sorted(answer)[N - 1])