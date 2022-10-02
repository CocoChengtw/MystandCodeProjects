"""
File: boggle.py
Name: Coco
----------------------------------------
This project is to create a boggle game,
by using the input characters to find and print out all possible combinations in the dictionary,
and count how many words being found in total.
"""

import time
import numpy as np

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	ans = game()
	print('There are', ans, 'words in total.')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def letter_input():
	legal = 1
	while legal == 1:
		l1 = input('1 row of letters: ')
		l1_n = l1.split(' ')
		if len(l1_n) != 4:
			print('Illegal input')
			break
		l2 = input('2 row of letters: ')
		l2_n = l2.split(' ')
		if len(l2_n) != 4:
			print('Illegal input')
			break
		l3 = input('3 row of letters: ')
		l3_n = l3.split(' ')
		if len(l3_n) != 4:
			print('Illegal input')
			break
		l4 = input('4 row of letters: ')
		l4_n = l4.split(' ')
		if len(l4_n) != 4:
			print('Illegal input')
			break
		legal = 0
	return l1_n, l2_n, l3_n, l4_n


def game():
	dic = read_dictionary()
	board = letter_input()
	ans_lst = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			board_map = np.zeros((4, 4))
			board_map[i][j] = 1
			ans = game_helper(i, j, board, board_map, dic, board[i][j], ans_lst)
	return ans


def game_helper(x, y, board, board_map, dic, cur_word, ans_lst):
	if len(cur_word) >= 4 and cur_word[0] in dic and cur_word in dic[cur_word[0]]:
		if cur_word not in ans_lst:
			ans_lst.append(cur_word)
			print(f'Found "{cur_word}"')
	for i in range(-1, 2):
		for j in range(-1, 2):
			# choose
			if 0 <= (x + i) < len(board) and 0 <= (y + j) < len(board[0]):
				if board_map[x + i][y + j] == 0:
					board_map[x + i][y + j] = 1
					cur_word += board[x + i][y + j]
					if len(cur_word) == 2:
						if has_prefix(cur_word, dic[cur_word[0]]):
							# explore
							game_helper(x + i, y + j, board, board_map, dic, cur_word, ans_lst)
					else:
						# explore
						game_helper(x + i, y + j, board, board_map, dic, cur_word, ans_lst)
					# un-choose
					cur_word = cur_word[:-1]
					board_map[x + i][y + j] = 0
	return len(ans_lst)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dic = {}
	with open(FILE, 'r')as f:
		for line in f:
			if line.strip()[0] not in dic:
				dic[line.strip()[0]] = [line.strip()]
			else:
				dic[line.strip()[0]].append(line.strip())
	return dic


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dic: (dic) A dictionary contains all words to look up
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in dic:
		if i.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
