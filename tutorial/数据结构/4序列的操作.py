# 切片 list，tuple，str都支持切片操作
nums = [0, 1, 2, 3, 4, 5]
# [:n] 表示取前n个 [n:]表示舍弃前n个 [n:m] 表示舍弃前n个，并取m-n个 [n:m:k]同[n:m] k表示从下个一个数，数k下取第k个
print(nums[:2], nums[2:], nums[2:2], nums[2:4], nums[2:][:3], nums[2:][:1])
s = 'bicycle'
print(s[1:5], s[1:5:3])

# 切片赋值
nums[1:4:2] = [0, 0]
print(nums)

# 序列使用+和*
s = 'ha'
print(s * 3)
print(s + "!")
