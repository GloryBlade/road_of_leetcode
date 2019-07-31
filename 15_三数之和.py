'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


def threeSum(nums):
	"""
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    res = []
    nums.sort()

    if len(nums)<3:
        return
    if nums[0]>0 or nums[-1]<0:
        return

    left = 0
    mid = 1
    right = len(nums)-1

    while mid < len(nums):
        if nums[left] + nums[mid] > 0:
            break
        tmp = nums[left] + nums[mid] + nums[right]
        if mid >= right:
            while left < mid-1 and nums[left] == nums[left+1]:   
                left = left+1
            left = left+1
            mid = left+1
            right = len(nums)-1
        elif tmp == 0:
            res.append([nums[left], nums[mid], nums[right]])
            while mid < right-2 and nums[mid] == nums[mid+1]:
                mid = mid+1
            mid = mid+1
            right = right-1
        elif tmp < 0:
            while nums[left] + nums[mid] + nums[right]<0 and mid<right:
                mid = mid+1
        elif tmp > 0:
            while nums[left] + nums[mid] + nums[right]>0 and mid<right:
                right = right-1

	return res
