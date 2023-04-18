In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Enter your code here. Read input from STDIN. Print output to STDOUT
S=input()
l=[]
k=[]
i=0

count=0
while i<len(S):
    count1=0
    for j in range(i,len(S)):
        if S[i]==S[j]:
            count1=count1+1
        else:
          break
    l.append((count1,int(S[i])))
    count=count+count1   
    i=count

for i in l:
  print(i,end=" ")
