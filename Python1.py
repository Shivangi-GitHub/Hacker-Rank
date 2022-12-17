'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

import sys
while True:
    n=int(input("enter n integer"))
    if n>=1 and n<=100000:
        m=int(input("Enter m integer"))
        if m>=1 and m<=100000:
            #print(n,end=" ")
            #print(m)
            break
l=[]   
for i in range(0,n):
    au=int(input("Enter: "))
    l.append(a)
k=np.array(l)
print(k) 

d=[]
f=[]
for j in range(0,m):
    v=int(input("enter :"))
    d.append(v)
for k in range(0,m):
    r=int(input("neter "))
    f.append(b)
a=np.array(d)
b=np.array(f)
    

count=0
c=0
for i in a:
  count=count+1
#print(count)

for i in b:
  c=c-1
  break
#print(c)

print(count+c)
