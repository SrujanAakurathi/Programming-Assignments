"""

Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order. 

Input Format:
The first line of the input contains N distinct integers of list A separated by a space.

Output Format
Print the minimum number of moves required to sort the elements.

Example:

Input:
1 3 2 4 5

Output:
3

"""

x=[int(x) for x in input().split()]
x1=sorted(x)
c=0
for i in range(len(x)):
    if x[i]==x1[c]:
        c=c+1
print(len(x)-c,end="")
