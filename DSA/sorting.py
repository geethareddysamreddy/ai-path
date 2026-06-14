def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

def get_input():
    while True:
        try:
            nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
            if len(nums) < 2:
                print("Enter at least 2 numbers!")
                continue
            return nums
        except ValueError:
            print("Invalid input! Enter numbers only.")

def main():
    print("=== Sorting Algorithms ===")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")

    choice = input("Choose (1/2/3): ").strip()
    nums = get_input()

    if choice == "1":
        print("Sorted:", bubble_sort(nums))
    elif choice == "2":
        print("Sorted:", selection_sort(nums))
    elif choice == "3":
        print("Sorted:", insertion_sort(nums))
    else:
        print("Invalid choice!")

main()