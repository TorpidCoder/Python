def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return True if len(set(nums)) < len(nums) else False

print(containsDuplicate(nums=[1,2,3]))