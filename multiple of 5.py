"""

Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.

Input Format:

The first line contains the numbers of list A separated by a space.

Output Format:

Print the numbers in a single line separated by a space which are not multiples of 5.

Example:

Input:

1 2 3 4 5 6 5

Output:

1 2 3 4 6

"""

print(*(item for item in map(int, input().split()) if item % 5), end=" ")
