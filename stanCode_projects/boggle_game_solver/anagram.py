"""
File: anagram.py
Name: Coco
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program is to search anagram words from the dictionary.
    """
    start = time.time()

    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        print('Searching...')
        final_lst = find_anagrams(word)
        print(len(final_lst), 'anagrams:', final_lst)

    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    Read the dictionary and save in a dict dataframe.
    """
    word_dict = {}
    with open(FILE, 'r')as f:
        for line in f:
            if line.strip()[0] not in word_dict:
                word_dict[line.strip()[0]] = [line.strip()]
            else:
                word_dict[line.strip()[0]].append(line.strip())
    return word_dict


def find_anagrams(s):
    """
    :param s: str, word being input by user
    :return: anagram words for s
    """
    word_dict = read_dictionary()
    word_dict_s = {}
    new_dict = {}
    for ch in s:
        word_dict_s[ch] = word_dict[ch]
    for i in word_dict_s:
        for j in range(len(word_dict_s[i])):
            if len(word_dict_s[i][j]) == len(s):
                if i not in new_dict:
                    new_dict[i] = [word_dict_s[i][j]]
                else:
                    new_dict[i].append(word_dict_s[i][j])

    final_lst = find_anagrams_helper(s, new_dict, [], '', len(s), [])
    return final_lst


def find_anagrams_helper(word, word_dict, curr_lst, curr_word, ans_len, final_lst):
    """
    This helper is to use back tracking algorithm to find out the anagrams from the dictionary.
    """
    if len(curr_lst) == ans_len:
        if curr_word in final_lst:
            pass
        elif curr_word in word_dict[curr_word[0]]:
            final_lst.append(curr_word)
            print('Found:', curr_word)
            print('Searching...')
    else:
        for w in range(len(word)):
            if w in curr_lst:
                pass
            else:
                # choose
                curr_lst.append(w)
                curr_word += word[w]
                if len(curr_lst) == 3:
                    if has_prefix(curr_word, word_dict[curr_word[0]]) is True:
                        # explore
                        find_anagrams_helper(word, word_dict, curr_lst, curr_word, ans_len, final_lst)
                else:
                    # explore
                    find_anagrams_helper(word, word_dict, curr_lst, curr_word, ans_len, final_lst)
                # un-choose
                curr_lst.pop()
                curr_word = curr_word[:-1]
    return final_lst


def has_prefix(sub_s, word_dict):
    """
    :param sub_s: str, the 2 starting character
    :return: boolean, to tell whether the starting characters are in the dictionary or not
    """
    # word_dict = read_dictionary()
    for i in word_dict:
        if i.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
