from newpackage import recursion, sorting

assert sorting.bubble_sort([3,8,3,9,4]) == [3,3,4,8,9], 'incorrect'
assert sorting.merge_sort([3,8,3,9,4]) == [3,3,4,8,9], 'incorrect'
assert sorting.quick_sort([3,8,3,9,4]) == [3,3,4,8,9], 'incorrect'

assert recursion.sum_array([1,2,3]) == 6, 'incorrect'
assert recursion.fibonacci(6) == 8, 'incorrect'
assert recursion.factorial(4) == 24, 'incorrect'
assert recursion.reverse('hello') == 'olleh', 'incorrect'

