def merge(nums1, m, nums2, n):
    """
    >>> l1, l2 = [1,2,3,0,0,0], [2,5,6]
    >>> merge(l1, 3, l2, 3)
    >>> l1
    [1,2,2,3,5,6]
    
    Do not return anything, modify nums1 in-place instead.
    """
    l1_data_index = m - 1
    l1_back_index = len(nums1) - 1

    for value in nums2[::-1]:
        while nums1[l1_data_index] > value and l1_data_index >= 0:
            nums1[l1_back_index] = nums1[l1_data_index]
            l1_back_index -= 1
            l1_data_index -= 1
        nums1[l1_back_index] = value
        l1_back_index -= 1
    return