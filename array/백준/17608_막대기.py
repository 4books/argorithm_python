"""
https://www.acmicpc.net/problem/17608
"""
def solution(sticks):
    answer = 1
    src = sticks.pop()
    for _ in range(len(sticks)):
        tgt = sticks.pop()
        if tgt > src:
            answer += 1
            src = tgt

    return answer


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
print(solution(arr))
