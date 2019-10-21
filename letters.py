"""

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9 

"""

t=input()
uc=0
lc=0
for i in t:
  if i.islower() :
    lc+=1
  elif i.isupper() :
    uc+=1
print(uc,lc)
