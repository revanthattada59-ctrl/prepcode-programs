nums = [1, 2, 3, 4]
tot = 0
n = len(nums)
for i in range(0, n):
    cur = i + 1
    if n % cur == 0:
        tot = tot + nums[i] ** 2
print(tot)
