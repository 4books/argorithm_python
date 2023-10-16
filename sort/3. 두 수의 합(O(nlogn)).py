def solution(nums, target):
    answer = []
    n = len(nums)
    minN = 1_000_000_000
    nums.sort()
    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        minN = min(diff, minN)

    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        if diff == minN:
            answer.append([nums[i - 1], nums[i]])

    return answer


print(solution([3, 7, 2, 12, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([11, 17, 6, 8, 21, 9, 19, 12, 25, 16, 2], 26))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))
