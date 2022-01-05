with open("5.TXT") as fp:
    nums = list(map(int, fp.readlines()))

# nums = [0, 3, 0, 1, -3]
i = 0
c = 0
print("  --nums --  " , nums)

while 0 <= i < len(nums):
    c += 1
    j = i + nums[i]
    nums[i] += 1 if nums[i] < 3 else -1
    i = j
print("  --count--  " , c)


#nope 29227751 is too high
