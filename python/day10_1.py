from file_ops import readlines
from collections import Counter


def main(nums):
    ordered = sorted(nums)
    ordered_both_ends = [0] + ordered + [max(nums) + 3]
    diffs = [ordered_both_ends[i + 1] - ordered_both_ends[i] for i in range(len(ordered_both_ends) - 1)]
    num_diffs = Counter(diffs)
    return num_diffs[1], num_diffs[2], num_diffs[3]


if __name__ == '__main__':
    nums = readlines(10, int)
    diffs = main(nums)
    print(diffs[0] * diffs[2])
