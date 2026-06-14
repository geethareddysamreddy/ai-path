# ============ Linear Search ============
def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# ============ Binary Search ============
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ============ Main ============
nums = [10, 25, 3, 47, 8]
print("Linear Search:")
print(linear_search(nums, 47))      # 3
print(linear_search(nums, 99))      # -1

nums_sorted = [3, 8, 10, 25, 47]
print("\nBinary Search:")
print(binary_search(nums_sorted, 25))   # 3
print(binary_search(nums_sorted, 99))   # -1