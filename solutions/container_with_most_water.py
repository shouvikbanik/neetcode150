def max_area(height):
    left = 0
    right = len(height) - 1
    maximum_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > maximum_area:
            maximum_area = area
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maximum_area
