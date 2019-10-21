"""

Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without quotes). 
Write a program to construct the lexicographically smallest palindrome by filling each of the faded character ('.') with a lower case alphabet.

Definition:
The smallest lexicographical order is an order relation where string s is smaller than t, given the first character of s (s1 ) is smaller than the first character of t (t1 ), or in case they
are equivalent, the second character, etc.

For example "aaabbb" is smaller than "aaac" because although the first three characters
are equal, the fourth character b is smaller than the fourth character c. 

Input Format: 
String S

Output Format: 
Print lexicographically smallest palindrome after filling each '.' character, if it
possible to construct one. Print -1 otherwise.

Example-1

Input:
a.ba

Output:
abba


Example-2:

Input:
a.b

Output:
-1

"""

x=list(input())
l=len(x)
if l%2==1:
    a=x[0:int(l/2)]
    b=x[int(l/2)+1:]
    b=b[::-1]
    Y="alk"
    for i in range(len(a)):
        if a[i]=="." and b[i]!=".":
            a[i]=b[i]
        elif b[i]=="." and a[i]!=".":
            b[i]=a[i]
        elif a[i]=="." and b[i]==".":
            a[i]="a"
            b[i]="a"
        elif a[i]!=b[i] or b[i]!=a[i]:
            print("-1")
            Y='fls'
            break
    if Y!="fls":
        b=b[::-1]
        s=a+["a"]+b
        print("".join(s))
    
else:
    a=x[0:int(l/2)]
    b=x[int(l/2):]
    b=b[::-1]
    Y="alk"
    for i in range(len(a)):
        if a[i]=="." and b[i]!=".":
            a[i]=b[i]
        elif b[i]=="." and a[i]!=".":
            b[i]=a[i]
        elif a[i]=="." and b[i]==".":
            a[i]="a"
            b[i]="a"
        elif a[i]!=b[i] or b[i]!=a[i]:
            print("-1")
            Y='fls'
            break
    if Y!="fls":
        b=b[::-1]
        s=a+b
        print("".join(s))
