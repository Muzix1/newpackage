from newpackage import recursion, sorting

def test_bubble_sort():
    """
    Ensuring that the sorting method works
    """
    assert sorting.bubble_sort([3,8,3,9,4]) == [3,3,4,8,9], 'incorrect'

def test_merge_sort():
    """
    Ensuring that the sorting method works
    """
    assert sorting.merge_sort([3,8,3,9,4]) == [3,3,4,8,9], 'incorrect'

def test_quick_sort():
    """
    Ensuring that the sorting method works
    """
    assert sorting.quick_sort([3,8,3,9,4]) == [3,3,4,8,9], 'incorrect'

def test_sum_array():
    """
    Ensuring that the sum_array works
    """
    assert recursion.sum_array([1,2,3]) == 6, 'incorrect'

def test_fibonacci():
    """
    Ensure that sum_array function works
    """
    assert recursion.fibonacci(6) == 8, 'incorrect'

def test_factorial():
    """
    Ensure that factorial function works
    """
    assert recursion.factorial(4) == 24, 'incorrect'

def test_reverse():
    """
    Ensure that reverse function works
    """
    assert recursion.reverse('hello') == 'olleh', 'incorrect'

