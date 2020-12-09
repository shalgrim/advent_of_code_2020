from file_ops import readlines

if __name__ == '__main__':
    nums = readlines(9, int)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            the_sum = sum(nums[i : j + 1])
            if the_sum >= 26796446:
                break
        if the_sum == 26796446:
            break
    print(min(nums[i : j + 1]) + max(nums[i : j + 1]))
