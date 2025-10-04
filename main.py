import sys
from typing import List


class lz77:

    def __init__(self, lookahead_window_size, search_window_size):
        self.lookahead_window_size = lookahead_window_size
        self.search_window_size = search_window_size

    def get_position_and_length(self, lookahead_window: [str], search_window: [str]):
        """returns the longest match in search window starting from lookahead_window,
         currently doesn't handle repeating at the end"""
        longest_match_length = 0
        longest_match_index = -1
        if len(lookahead_window) == 0:
            return 0, 0
        for i in range(len(search_window)):
            if lookahead_window[0] == search_window[i]:
                j = 1
                while (j < len(lookahead_window)
                       and self.search_window_size > len(search_window) > i + j
                       and lookahead_window[j] == search_window[i + j]):
                    j += 1
                if longest_match_length < j:
                    longest_match_length = j
                    longest_match_index = i
        if longest_match_index != -1:
            longest_match_index = len(search_window) - longest_match_index
        else:
            longest_match_index = 0
        return longest_match_index, longest_match_length

    def construct_lookahead_window(self, string_to_be_compressed: str, index: int):
        lookahead_window = []
        for i in range(index, min(len(string_to_be_compressed), self.lookahead_window_size + index)):
            lookahead_window.append(string_to_be_compressed[i])
        return lookahead_window

    def construct_search_window(self, string_to_be_compressed: str, index: int):
        lookahead_window = []
        for i in range(index - 1, -1, -1):
            if len(lookahead_window) == self.lookahead_window_size:
                break
            lookahead_window.append(string_to_be_compressed[i])
        lookahead_window.reverse()
        return lookahead_window

    def compress(self, string_to_be_compressed: str) -> [[int, int, str]]:
        returned_compressed_string: [[int, int, str]] = []
        i = 0
        while i < len(string_to_be_compressed):
            search_window = self.construct_search_window(string_to_be_compressed, i)
            lookahead_window = self.construct_lookahead_window(string_to_be_compressed, i)
            position, length = self.get_position_and_length(lookahead_window, search_window)
            if i + length < len(string_to_be_compressed):
                returned_compressed_string.append([position, length, string_to_be_compressed[i + length]])
            else:
                returned_compressed_string.append([position, length, '\0'])
            if len(search_window) > self.search_window_size:
                search_window.pop(0)
            i += max(length + 1, 1)

        return returned_compressed_string


    def decompress(self, compressed_string: [[int, int, str]]) -> str:
        return 'a'


if __name__ == '__main__':
    NUM_LOCATION_BITS = 3
    NUM_POSITION_BITS = 3
    LOOKAHEAD_WINDOW_SIZE = 2 ** NUM_LOCATION_BITS
    SEARCH_WINDOW_SIZE = 2 ** NUM_POSITION_BITS
    lz = lz77(LOOKAHEAD_WINDOW_SIZE, SEARCH_WINDOW_SIZE)

    input_string = 'ABAABABAABBBBBBBBBBBBA' # lecture 1 example; slide 19.
    compressed_string = lz.compress(input_string)
    decompressed_string = lz.decompress(compressed_string)
    print('input_string: ', input_string)
    print('size of input_string: ', sys.getsizeof(compressed_string))
    print('compressed_string: ', compressed_string)
    print('size of compressed_string: ', sys.getsizeof(compressed_string))
    print('decompressed_string: ', decompressed_string)
    print('size of decompressed_string: ', sys.getsizeof(decompressed_string))
