num = 1
count = sum(x % 2 == 0 for x in range(num, 100))
print(f"1-100之间有{count}个偶数")
