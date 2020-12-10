from file_ops import readlines


def count_arrangements(nums, start=0, target=None):
    if target is None:
        target = max(nums)

    answer = 0
    potentials = [n for n in nums if 1 <= n-start <= 3]

    for potential in potentials:
        if potential == target:
            answer += 1
        else:
            answer += count_arrangements(nums, potential, target)

    return answer


if __name__ == '__main__':
    nums = readlines(10, int)
    nums += [max(nums) + 3]
    print(count_arrangements(nums))
