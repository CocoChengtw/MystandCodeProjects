"""
File: largest_digit.py
Name: Coco
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the input number could be either positive or negative number
	:return: int, the biggest number of the input numbers
	"""
	return find_largest_digit_help(abs(n), 0)


def find_largest_digit_help(n, big_n):
	"""
	This helper is to find the biggest number
	"""
	if n / 10 < 0.1:
		return big_n
	else:
		n1 = n % 10
		n = n // 10
		if n1 > big_n:
			big_n = n1
		return find_largest_digit_help(n, big_n)


if __name__ == '__main__':
	main()
