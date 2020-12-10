from functools import lru_cache

from file_ops import readlines


def count_arrangements(nums):
    @lru_cache
    def helper(start, target):

        answer = 0
        potentials = [n for n in nums if 1 <= n-start <= 3]

        for potential in potentials:
            if potential == target:
                answer += 1
            else:
                answer += helper(potential, target)

        return answer
    return helper(0, max(nums))


if __name__ == '__main__':
    nums = readlines(10, int)
    nums += [max(nums) + 3]
    print(count_arrangements(nums))
