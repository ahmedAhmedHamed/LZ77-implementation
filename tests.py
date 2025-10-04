from main import lz77

lz = lz77(3, 3)

inp = '123456789abcdefg'
print(len(inp))
assert lz.construct_lookahead_window(inp, 0) == ['1', '2', '3']
assert lz.construct_lookahead_window(inp, 1) == ['2', '3', '4']
assert lz.construct_lookahead_window(inp, 3) == ['4', '5', '6']
assert lz.construct_lookahead_window(inp, 15) == ['g']
assert lz.construct_lookahead_window(inp, 14) == ['f', 'g']
assert lz.construct_lookahead_window(inp, 13) == ['e', 'f', 'g']

assert lz.construct_search_window(inp, 0) == []
assert lz.construct_search_window(inp, 1) == ['1']
assert lz.construct_search_window(inp, 3) == ['1', '2', '3']
assert lz.construct_search_window(inp, 15) == ['d', 'e', 'f']
assert lz.construct_search_window(inp, 14) == ['c', 'd', 'e']
assert lz.construct_search_window(inp, 13) == ['b', 'c', 'd']


