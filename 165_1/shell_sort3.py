def shell_sort3(nums):
	if len(nums) > 1:
		n = len(nums)
		gaps = [8589934592, 4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 243, 216, 192, 162, 144, 128, 108, 96, 81, 72, 64, 54, 48, 36, 32, 27, 24, 18, 16, 12, 9, 8, 6, 4, 3, 2, 1]

		for gap in gaps:
			if gap < n:
				for i in range(len(nums)-gap):
					j = i + gap
					while (j > 0 and nums[j] < nums[j-gap]):
						nums[j], nums[j-gap] = nums[j-gap], nums[j]
						j -= gap
	return nums

