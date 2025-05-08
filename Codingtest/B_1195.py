import sys

input = sys.stdin.readline

part1 = input().strip()
part2 = input().strip()

if len(part1) > len(part2):
    part1, part2 = part2, part1

meet_thing = 0
for k in range(len(part1)):
    for i in range(k+1):
        if part1[-k+i-1] == '2' and part2[i] == '2':
            break
    else:
        meet_thing = max(meet_thing, k + 1)


    for i in range(k+1):
        if part1[i] == '2' and part2[-k+i-1] == '2':
            break
    else:
        meet_thing = max(meet_thing, k + 1)

for k in range(len(part2) - len(part1) + 1):
    for i in range(len(part1)):
        if part1[i] == '2' and part2[i + k] == '2':
            break
    else:
        meet_thing = max(meet_thing, len(part1))
        break

print(len(part1) + len(part2) - meet_thing)