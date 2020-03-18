# 1
def count_evens(nums):
	even = 0
	for i in nums:
		if i % 2 == 0:
			even += 1

	return even


# 2
def big_diff(nums):
	return max(nums) - min(nums)


# 3
def centered_average(nums):
	maxx = max(nums)
	minn = min(nums)

	sum = 0 - maxx - minn
	for i in nums:
		sum += i

	# return sum
	return sum / (len(nums) - 2)


# 4
def sum13(nums):
	sum = 0
	isThirt = False
	for num in nums:
		if num == 13:
			isThirt = True
		if isThirt == False:
			sum += num
		if isThirt == True and num != 13:
			isThirt = False

	return sum


# 5

def firstDigit(n):
	while n >= 10:
		n = n / 10;
	return int(n)


def sum67(nums):
	sum = 0
	isSix = False
	for num in nums:
		if firstDigit(num) == 6:
			isSix = True
		if num == 7 and isSix == True:
			isSix = False
		elif isSix == False:
			sum += num
	return sum


# 6

def has22(nums):
	isTwo = False
	for num in nums:
		if num == 2 and isTwo == False:
			isTwo = True
		elif num == 2 and isTwo == True:
			return True
		elif num != 2:
			isTwo = False
	return False
