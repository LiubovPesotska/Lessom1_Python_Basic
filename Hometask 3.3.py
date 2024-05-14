numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_list =[]
nums_len = len(numbers)
middle_index=nums_len//2
print(middle_index)
if nums_len==0:
    result_list.append([])
    result_list.append([])
    print(result_list)
elif nums_len%2!=0:
    nums1 = numbers[:middle_index+1]
    nums2 = numbers[middle_index+1:]
    result_list.append(nums1)
    result_list.append(nums2)
    print(result_list)
else:
    nums1 = numbers[:middle_index]
    nums2 = numbers[middle_index:]
    result_list.append(nums1)
    result_list.append(nums2)
    print(result_list)


