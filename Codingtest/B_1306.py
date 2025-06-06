import sys

if __name__ == '__main__':
    N = int(input())
    q = []
    now = ''
    for _ in range(N):
        flag = False
        cmd, ch, t = map(str, sys.stdin.readline().split())
        if cmd == 'type':
            now += ch
            q.append((int(t), now))
        else:
            ch, t = int(ch), int(t)
            for i in range(len(q) - 1, -1, -1):
                if q[i][0] >= t - ch: continue
                flag = True
                now = q[i][1]
                q.append((t, now))
                break
            if not flag:
                now = ''
                q.append((t, now))
    print(q[-1][1])