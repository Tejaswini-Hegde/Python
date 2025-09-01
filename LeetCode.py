

nums1 = [1, 2]

nums2 = [3, 4]
m = len(nums1)
n = len(nums2)

print(m, n)
t = m+n
print(t)
val1 = 0
for i in nums1:
    val1 += i
print(val1)
val2 = 0
for j in nums2:
    val2 += j
print(val2)
s = val1+val2
t = n+m
d = float(s/t)
print(d)
