def product_except_self(nums):
    prefix_product = [1]
    suffix_product = [1]
    left = 1
    right = len(nums) - 2
    prefix_val = 1
    suffix_val = 1
    while left != len(nums):
        prefix_product.append(nums[left - 1] * prefix_val)
        suffix_product = [nums[right + 1] * suffix_val] + suffix_product
        prefix_val = nums[left - 1] * prefix_val
        suffix_val = nums[right + 1] * suffix_val
        left += 1
        right -= 1
    product_list = []
    for index in range(len(prefix_product)):
        product_list.append(prefix_product[index] * suffix_product[index])
    return product_list
