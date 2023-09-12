"""
청소 로봇은 다음 규칙에 따라 이동합니다.
1. 'U' 명령은 로봇이 위쪽으로 한 칸 이동합니다.
2. 'R' 명령은 로봇이 오른쪽으로 한 칸 이동합니다.
3. 'L' 명령은 로봇이 왼쪽으로 한 칸 이동합니다.
4. 'D' 명령은 로봇이 아래쪽으로 한 칸 이동합니다.
매개변수 moves에 청소 로봇에 명령을 내린 문자들이 차례대로 나열된 명령 문자열이 주어지
면 이 명령 문자열을 청소 로봇이 모두 수행했을 때 최종 위치를 반환하는 프로그램을 작성하
세요. 격자판 밖으로 벗어나는 명령은 주어지지 않습니다.
"""


def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']
    for c in moves:
        for k in range(4):
            if c == dir[k]:
                x = x + dx[k]
                y = y + dy[k]

    return [x, y]


print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
