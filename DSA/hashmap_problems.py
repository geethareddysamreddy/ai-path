# ============ Problem 1 - Two Sum ============
def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in seen:
            return f"Indices: [{seen[need]}, {i}] → {need}+{nums[i]}={target}"
        seen[nums[i]] = i

# ============ Problem 2 - Find Duplicates ============
def find_duplicates(nums):
    d = {}
    for num in nums:
        d[num] = d[num] + 1 if num in d else 1
    return [num for num in d if d[num] > 1]

# ============ Problem 3 - First Non Repeating ============
def first_non_repeating(s):
    d = {}
    for char in s:
        d[char] = d[char] + 1 if char in d else 1
    for char in s:
        if d[char] == 1:
            return char

# ============ Problem 4 - Group Anagrams ============
def group_anagrams(words):
    d = {}
    for word in words:
        key = "".join(sorted(word))
        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]
    return list(d.values())

# ============ Problem 5 - Most Frequent ============
def most_frequent(nums):
    d = {}
    for num in nums:
        d[num] = d[num] + 1 if num in d else 1
    return max(d, key=d.get)

# ============ Main ============
print(two_sum([2, 7, 11, 15], 9))
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
print(first_non_repeating("aabbcddeff"))
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(most_frequent([1, 3, 2, 1, 4, 1, 3, 3, 3]))