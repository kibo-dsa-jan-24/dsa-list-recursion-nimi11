# Recursive List Functions

In this exercise, you will use recursion to write some functions that manipulate lists.

## Your Task

In `list_recursion.py`, you will find stub implementations of various list functions. You should implement each one of these functions recursively -- without any loops.

The functions are:

1. `print_sentence(lst)`: accepts a list parameter `lst` and prints the elements of the list as if they were a sentence, punctuated with a period. For example, `print_sentence(['The', 'quick', 'brown', 'fox'])` should print the string `The quick brown fox.`

  * The last string in the list should have a period printed after it.
  * If `lst` is `None` or the empty list, nothing should be printed.

2. `reverse(lst)`: accepts a list parameter `lst` and returns a list with all of the same elements of `lst`, but with their order reversed.

  * If `lst` is `None` or the empty list, `lst` should be returned.

3. `remove_every_other(lst)`: accepts a list parameter `lst` and returns a version of the list with every other element removed. For example, `remove_every_other(['The', 'quick', 'brown', 'fox'])` should return `['The', 'brown']`.

  * If `lst` is `None` or the empty list, `lst` should be returned.

4. `maximum(lst)`: accepts a list parameter `lst` of numbers, and returns the maximum number in the list. For example, `maximum([5, 99, 3, 25, 50])` should return `99`.

  * If `lst` is `None` or the empty list, `None` should be returned.

## Testing

The file `test_list_recursion.py` contains some unit tests for the functions, but the tests aren't comprehensive. You should think of other applicable test cases (especially those that evaluate corner cases) and add them.
