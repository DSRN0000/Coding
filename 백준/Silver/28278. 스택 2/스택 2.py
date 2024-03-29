import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    command = sys.stdin.readline().rstrip()

    #push
    if len(command) > 2:
        stack.append(int(command[2:]))

    #pop
    elif command == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    #size
    elif command == '3':
        print(len(stack))

    #empty
    elif command == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    #top
    elif command == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])