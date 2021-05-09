n, m, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

cnt1 = k * (int(m/(k+1))) + m % (k+1)
cnt2 = int(m/(k+1))

sum = cnt1 * nums[n-1] + cnt2 * nums[n-2]
print(sum)
