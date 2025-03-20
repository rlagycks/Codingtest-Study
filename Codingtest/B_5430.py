import json
import sys
from collections import deque

def process_commands(commands, array):
    is_reversed = False

    for cmd in commands:
        if cmd == "R":
            is_reversed = not is_reversed
        elif cmd == "D":
            if not array:
                print("error")
                return
            if is_reversed:
                array.pop()
            else:
                array.popleft()
    if is_reversed:
        array.reverse()

    print("[" + ",".join(map(str, array)) + "]")

T = int(sys.stdin.readline().strip())
for _ in range(T):
    commands = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    array_input = sys.stdin.readline().strip()

    if n == 0:
        array = deque()
    else:
        array = deque(json.loads(array_input))

    process_commands(commands, array)