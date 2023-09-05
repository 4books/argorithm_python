from collections import deque


def test_deque():
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)
    print(dq)
    dq.pop()
    print(dq)

    dq.clear()

    dq.appendleft(1)
    dq.appendleft(2)
    dq.appendleft(3)
    print(dq)
    dq.popleft()
    print(dq)


if __name__ == '__main__':
    test_deque()
