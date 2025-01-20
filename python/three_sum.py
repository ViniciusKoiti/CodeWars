def find_sum_three(nums, target):
    for i in range(len(nums)):
        needed = target - nums[i]
        seen =  set()
        for j in range(i+i, len(nums)):
            complement = needed - nums[j]
            if complement in seen:
                return True
            seen.add(nums[j])
    return False