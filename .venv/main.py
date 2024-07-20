n3=sorted(nums1[:m]+nums2[:n])
for i in range (m+n): nums1[i]=n3[i]
return (nums1)