import code_344_reverse_string as c1

def test_example_1():
    s = c1.Solution()
    arr = ['h','e','l','l','o']
    s.reverseString(arr)
    assert arr == ['o','l','l','e','h']

def test_example_2():
    s = c1.Solution()
    arr = ["H","a","n","n","a","h"]
    s.reverseString(arr)
    assert arr == ["h","a","n","n","a","H"]