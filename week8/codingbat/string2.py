# 1
def double_char(str):
	ans = ""
	for char in str:
		ans += 2 * char
	return ans


# 2
def count_hi(str):
	return str.count('hi')


# 3
def cat_dog(str):
	cat = str.count('cat')
	dog = str.count('dog')

	if cat == dog:
		return True
	else:
		return False


# 4
def count_code(str):
	result = 0
	for i in range(len(str) - 3):
		if str[i:i + 2] == 'co' and str[i + 3] == 'e':
			result += 1
	return result


# 5
def end_other(a, b):
	s = []

	if len(a) < len(b):
		s = b[-len(a):]
		if s.lower() == a.lower():
			return True
		else:
			return False
	else:
		s = a[-len(b):]
		if s.lower() == b.lower():
			return True
		else:
			return False


# 6

def xyz_there(str):
	if 'xyz' in str and '.xyz' not in str: return True
	if str.count('xyz') > str.count('.xyz'):
		return True
	else:
		return False
