# ============ Problem 1 - Max & Min ============
def find_max_min(nums):
    max_val = nums[0]
    min_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(f"Maximum: {max_val}, Minimum: {min_val}")

# ============ Problem 2 - Reverse List ============
def reverse_list(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1          # ✅ no comma!
    print(nums)

# ============ Problem 3 - Second Largest ============
def second_largest(nums):
    largest = nums[0]
    second = nums[0]
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num < largest:
            second = num
    print(f"Largest: {largest}, Second Largest: {second}")

# ============ Problem 4 - Remove Duplicates ============
def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    print(result)

# ============ Problem 5 - Rotate List ============
def rotate_list(nums, k):
    n = len(nums)
    result = nums[n-k:] + nums[:n-k]
    print(result)

# ============ Main ============
find_max_min([3, 7, 1, 9, 4])
reverse_list([1, 2, 3, 4, 5])
second_largest([3, 7, 1, 9, 4])
remove_duplicates([1, 2, 2, 3, 4, 4, 5])
rotate_list([1, 2, 3, 4, 5], 2)