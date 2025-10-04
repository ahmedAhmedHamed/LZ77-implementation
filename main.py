import sys
from typing import List


def lz_compress(string_to_be_compressed: str, search_window_size, lookahead_window_size) -> [[int, int, str]]:
    return [[0, 0, 'a']]


def lz_decompress(compressed_string: [[int, int, str]]) -> str:
    return 'a'


if __name__ == '__main__':
    NUM_LOCATION_BITS = 3
    NUM_POSITION_BITS = 3
    LOOKAHEAD_WINDOW_SIZE = 2 ** NUM_LOCATION_BITS
    SEARCH_WINDOW_SIZE = 2 ** NUM_POSITION_BITS

    input_string = 'hello_world'
    compressed_string = lz_compress(input_string, SEARCH_WINDOW_SIZE, LOOKAHEAD_WINDOW_SIZE)
    decompressed_string = lz_decompress(compressed_string)
    print('input_string: ', input_string)
    print('size of input_string: ', sys.getsizeof(compressed_string))
    print('compressed_string: ', compressed_string)
    print('size of compressed_string: ', sys.getsizeof(compressed_string))
    print('decompressed_string: ', decompressed_string)
    print('size of decompressed_string: ', sys.getsizeof(decompressed_string))
