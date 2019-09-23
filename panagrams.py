"""

A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES

"""


p = []
for alphabet in range(97,123):
  p.append(chr(alphabet))
t = input()
t = t.lower()
u = set(t)
u = list(u)
for k in u:
  if k in p:
    p.remove(k)
if len(p)==0:
  print("YES")
else:
  print("NO")
