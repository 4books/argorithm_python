"""
빈도수(ver 1)
매개변수 nums에 길이가 n인 수열이 주어지면 수열의 원소중에서 빈도수가 1인 가장 큰 숫자
를 반환하는 프로그램을 작성하세요. 빈도수 1인 숫자가 없을 경우 -1를 반환하세요.
"""


def solution2(nums):
    answer = -1
    dic = dict()
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1

    for key, value in dic.items():
        if value == 1 and key > answer:
            answer = key

    return answer


def solution(nums: list[int]) -> int:
    answer = -1
    cnt = [0] * 1001
    for num in nums:
        cnt[num] += 1
    for i in range(1000, 0, -1):
        if cnt[i] == 1:
            return i
    return answer


print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
